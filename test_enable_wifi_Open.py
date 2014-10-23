from gaiatest import GaiaTestCase
import sys,time

class TestWpaWlan(GaiaTestCase):       
    
    def setUp(self):
        GaiaTestCase.setUp(self)
        sys.path.append("./")
        sys.path.append("./tests/functional/WPA-EAP")

    def test_enable_wifi(self):

        import WPA
        wpaObj = WPA.WpaEap(self.marionette)
        wpaObj.enableWifi()
        wpaObj.selectWPANetwork(self.testvars['wifi']['ssid'])
        time.sleep(3)                
      
        
        networkName = wpaObj.getActiveNetworkName()
        ''' v2.0
        self.assertEqual(networkName, 'Mozilla Guest')
      
        networkStatus = wpaObj.getActiveNetworkStatus()
        self.assertEqual(networkStatus, 'Connected')
        '''
        
        #v2.1
        self.assertIn(self.testvars['wifi']['ssid'],networkName)
                
        #forget wifi network
        wpaObj.forgetNetwork(self.testvars['wifi']['ssid'])