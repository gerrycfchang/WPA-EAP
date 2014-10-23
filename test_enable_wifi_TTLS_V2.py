from gaiatest import GaiaTestCase
import sys

class TestWpaWlan(GaiaTestCase):
   
    def setUp(self):
        GaiaTestCase.setUp(self)  
        sys.path.append("./")
        sys.path.append("./tests/functional/WPA-EAP")

    def test_enable_wifi(self):
        import WPA
        wpaObj = WPA.WpaEap(self.marionette)
        wpaObj.enableWifi()
        wpaObj.selectWPANetwork(self.testvars['wifi']['TTLS']['ssid'])
        wpaObj.selectEAPMethod('TTLS')
        wpaObj.choosePhase2Auth('MSCHAP V2')
        wpaObj.inputIdentity(self.testvars['wifi']['TTLS']['username'])
        wpaObj.inputPassword(self.testvars['wifi']['TTLS']['password'])
        wpaObj.join()
        
        networkName = wpaObj.getActiveNetworkName()        
        #v2.0
        #self.assertEqual(networkName, 'TPE_QA')
        
        #v2.1
        self.assertIn(self.testvars['wifi']['TTLS']['ssid'],networkName)
        
        networkStatus = wpaObj.getActiveNetworkStatus()
        self.assertEqual(networkStatus, 'Connected')
                
        #forget wifi network
        wpaObj.forgetNetwork(self.testvars['wifi']['TTLS']['ssid'])