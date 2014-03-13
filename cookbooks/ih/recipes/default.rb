#
# Cookbook Name:: ih
# Recipe:: default
#
# Copyright 2014, Example Com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

execute "apt-get-update" do
  command "apt-get update -y"
  ignore_failure true
  action :nothing
end

package "update-notifier-common" do
  notifies :run, resources(:execute => "apt-get-update"), :immediately
end

execute "apt-get-update-periodic" do
  command "apt-get update"
  ignore_failure true
  only_if do
   File.exists?('/var/lib/apt/periodic/update-success-stamp') &&
   File.mtime('/var/lib/apt/periodic/update-success-stamp') < Time.now - 86400
  end
end

%w{build-essential python-dev python-setuptools liblapack-dev liblapack3gf libgtk2.0-dev gfortran libblas3gf liblapack3gf libopencv-dev libopencv-highgui-dev libcvaux-dev python-opencv python-setuptools python-virtualenv}.each do |pkg|
    package pkg do
      action :install
    end
end

user node[:ih][:user] do
  action :create
  system true
  shell "/bin/false"
end

directory node[:ih][:dir] do
  owner "root"
  mode "0755"
  action :create
end

directory node[:ih][:data_dir] do
  owner "ih"
  mode "0755"
  action :create
end

directory node[:ih][:log_dir] do
  mode 0755
  owner node[:ih][:user]
  action :create
end

#remote_file "#{Chef::Config[:file_cache_path]}/ih.tar.gz" do
#  source "https://github.com/antirez/ih/tarball/v2.0.4-stable"
#  action :create_if_missing
#end

bash "compile_ih_source" do
  cwd Chef::Config[:file_cache_path]
  code <<-EOH
    echo "Can I has sources to compile"
  EOH
  creates "/usr/local/bin/ih-service"
end

service "ih" do
  provider Chef::Provider::Service::Upstart
  subscribes :restart, resources(:bash => "compile_ih_source")
  supports :restart => true, :start => true, :stop => true
end

template "ih.conf" do
  path "#{node[:ih][:dir]}/ih.conf"
  source "ih.conf.erb"
  owner "root"
  group "root"
  mode "0644"
  notifies :restart, resources(:service => "ih")
end

template "ih.upstart.conf" do
  path "/etc/init/ih.conf"
  source "ih.upstart.conf.erb"
  owner "root"
  group "root"
  mode "0644"
  notifies :restart, resources(:service => "ih")
end

service "ih" do
  action [:enable, :start]
end
