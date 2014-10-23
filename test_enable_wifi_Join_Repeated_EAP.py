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
        for x in range(10):
            wpaObj.selectWPANetwork(self.testvars['wifi']['PEAP']['ssid'])
            wpaObj.selectEAPMethod('PEAP')        
            wpaObj.inputIdentity(self.testvars['wifi']['PEAP']['username'])
            wpaObj.inputPassword(self.testvars['wifi']['PEAP']['password'])
            wpaObj.join()                
        
            networkName = wpaObj.getActiveNetworkName()
            
            #v2.0
            #self.assertEqual(networkName, 'TPE_QA')
        
            #v2.1
            self.assertIn(self.testvars['wifi']['PEAP']['ssid'],networkName)

            #forget wifi network
            wpaObj.forgetNetwork(self.testvars['wifi']['PEAP']['ssid'])
        
            time.sleep(3)
        