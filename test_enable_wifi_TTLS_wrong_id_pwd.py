from gaiatest import GaiaTestCase
from gaiatest.apps.settings.app import Settings
from marionette.by import By
import sys
import time

class TestWpaWlan(GaiaTestCase):
       
    
    def setUp(self):
        GaiaTestCase.setUp(self)  
        sys.path.append("./")          

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
        wpaObj.selectWPANetwork('TPE_QA')
        wpaObj.selectEAPMethod('TTLS')
        wpaObj.inputIdentity('test')
        wpaObj.inputPassword('test')
        wpaObj.join()
        
        #import pdb; pdb.set_trace()
        time.sleep(3)
        networkName = wpaObj.getActiveNetworkName()
        self.assertNotEqual(networkName, 'TPE_QA')
        
        networkStatus = wpaObj.getActiveNetworkStatus()
        self.assertNotEqual(networkStatus, 'Connected')                
        