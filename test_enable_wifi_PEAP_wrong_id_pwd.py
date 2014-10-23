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
        wpaObj.selectWPANetwork(self.testvars['wifi']['PEAP']['ssid'])
        wpaObj.selectEAPMethod('PEAP')
        wpaObj.inputIdentity('test')
        wpaObj.inputPassword('test')
        wpaObj.join()
                
        networkStatus = wpaObj.getActiveNetworkStatus()
        self.assertNotEqual(networkStatus, 'Connected')