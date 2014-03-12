VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise32"
   config.vm.provision :chef_solo do |chef|
     chef.cookbooks_path = "cookbooks"
     chef.add_recipe "ih"
     chef.log_level = :debug
  end 
end
