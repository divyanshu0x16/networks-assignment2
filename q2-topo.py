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
        cHost = self.addHost( 'hC' )
        dHost = self.addHost( 'hD' )

        # Adding switches
        rOneSwitch = self.addSwitch( 'r1' )
        rTwoSwitch = self.addSwitch( 'r2' )

        # Add links
        self.addLink( aHost, rOneSwitch, cls=TCLink, bw=1000, delay='1ms')
        self.addLink( dHost, rOneSwitch, cls=TCLink, bw=1000, delay='1ms')
        self.addLink( bHost, rTwoSwitch, cls=TCLink, bw=1000, delay='1ms')
        self.addLink( cHost, rTwoSwitch, cls=TCLink, bw=1000, delay='1ms')
        self.addLink( rOneSwitch, rTwoSwitch, cls=TCLink, bw=500, delay='10ms')

topos = { 'mytopo': ( lambda: MyTopo() ) }