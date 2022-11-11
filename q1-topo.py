"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""
from mininet.topo import Topo
from mininet.link import TCLink

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Adding Hosts
        aHost = self.addHost( 'hA' )
        bHost = self.addHost( 'hB' )

        # Adding switches
        rOneSwitch = self.addSwitch( 'r1' )

        # Add links
        self.addLink( aHost, rOneSwitch)
        self.addLink( bHost, rOneSwitch)

topos = { 'mytopo': ( lambda: MyTopo() ) }