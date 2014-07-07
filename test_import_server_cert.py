from gaiatest import GaiaTestCase
from gaiatest.apps.settings.app import Settings
from marionette.by import By
import sys
import subprocess
import time

class TestWpaWlan(GaiaTestCase):       
    
    def setUp(self):
        GaiaTestCase.setUp(self)
        sys.path.append("./")
        sys.path.append("./tests/functional/WPA-EAP")

    def test_enable_wifi(self):
        #copy certs into sdcard
        subprocess.Popen(["sh","./prepareEnv.sh"])   
        time.sleep(1)
        
        settings = Settings(self.marionette)
        settings.launch()
        wifiObj = settings.open_wifi_settings()
        
        _wifi_enabled_checkbox_locator = (By.CSS_SELECTOR, '#wifi-enabled input')
        
        checkbox = self.marionette.find_element(*_wifi_enabled_checkbox_locator)
        if not checkbox.is_selected():
            wifiObj.enable_wifi()
        
        import WPA
        srvObj = WPA.SrvCertOp(self.marionette)
        srvObj.importSrvCert('gogogo')
        srvObj.deleteSrvCert('gogogo')
        srvObj.importSrvCert('cacert')
        srvObj.deleteSrvCert('cacert')
        
        
        
        