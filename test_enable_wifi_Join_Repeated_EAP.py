from gaiatest import GaiaTestCase
from gaiatest.apps.settings.app import Settings
from marionette.by import By
import sys,time

class TestWpaWlan(GaiaTestCase):       
    
    def setUp(self):
        GaiaTestCase.setUp(self)
        sys.path.append("./")
        sys.path.append("./tests/functional/WPA-EAP")

    def test_enable_wifi(self):
        settings = Settings(self.marionette)
        settings.launch()
        wifiObj = settings.open_wifi_settings()
        
        _wifi_enabled_checkbox_locator = (By.CSS_SELECTOR, '#wifi-enabled input')
        
        checkbox = self.marionette.find_element(*_wifi_enabled_checkbox_locator)
        if not checkbox.is_selected():
            wifiObj.enable_wifi()        
 
        import WPA
        wpaObj = WPA.WpaEap(self.marionette)
        for x in range(2):
            wpaObj.selectWPANetwork('TPE_QA')
            wpaObj.selectEAPMethod('PEAP')        
            wpaObj.inputIdentity('sqa')
            wpaObj.inputPassword('password')
            wpaObj.join()                
        
            networkName = wpaObj.getActiveNetworkName()        
            self.assertEqual(networkName, 'TPE_QA')        
        
            networkStatus = wpaObj.getActiveNetworkStatus()
            self.assertEqual(networkStatus, 'Connected')
                
            #forget wifi network
            wpaObj.forgetNetwork('TPE_QA')
        
            time.sleep(3)
        