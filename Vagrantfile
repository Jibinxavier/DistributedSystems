servers=[
 
  {
    :hostname => "test", 
    :box => "centos/7",
    :ram => 1024,
    :cpu => 1
  }
]

 
 

Vagrant.configure(2) do |config|  
    servers.each do |machine|
        config.vm.define machine[:hostname] do |node|
        
            node.vm.box = machine[:box]
            node.vm.hostname = machine[:hostname]
            node.vm.network "private_network", type: "dhcp"
            node.vm.provider "virtualbox" do |vb|
                vb.customize ["modifyvm", :id, "--memory", machine[:ram]]
            end

          
        end
    end
end