from gaiatest import GaiaTestCase
import sys,time

class TestWpaWlan(GaiaTestCase):       
    
    def setUp(self):
        GaiaTestCase.setUp(self)
        sys.path.append("./")
        sys.path.append("./tests/functional/WPA-EAP")

    def test_enable_wifi(self):
        ''' v2.0
        settings = Settings(self.marionette)
        settings.launch()
        wifiObj = settings.open_wifi_settings()
        
        _wifi_enabled_checkbox_locator = (By.CSS_SELECTOR, '#wifi-enabled input')
        
        checkbox = self.marionette.find_element(*_wifi_enabled_checkbox_locator)
        if not checkbox.is_selected():
            wifiObj.enable_wifi()        
        '''
        
        import WPA
        # v2.1
        wpaObj = WPA.WpaEap(self.marionette)
        wpaObj.enableWifi()
        
        wpaObj = WPA.WpaEap(self.marionette)
        wpaObj.selectWPANetwork(self.testvars['wifi']['PSK']['ssid'])
        wpaObj.inputPassword(self.testvars['wifi']['PSK']['password'])
        wpaObj.join()                
      
        networkName = wpaObj.getActiveNetworkName()
        ''' v2.0
        self.assertEqual(networkName, 'Mozilla Mobile')
      
        networkStatus = wpaObj.getActiveNetworkStatus()
        self.assertEqual(networkStatus, 'Connected')
        '''
        #v2.1
        self.assertIn('Mozilla Mobile',networkName)
        
        method = wpaObj.getStatusSecurityMethod()
        self.assertEqual(method, 'WPA-PSK')
        time.sleep(1)
        
        ipAddress = wpaObj.getStatusIP()
        self.assertRegexpMatches(ipAddress, "10.*.*.*")
        time.sleep(1) 
        
        signal = wpaObj.getStatusSignalStrengh()
        self.assertNotEqual(signal, "")
        time.sleep(1)
        
        speed = wpaObj.getStatusSpeed()
        self.assertNotEqual(speed, "")
        time.sleep(1)

        #forget wifi network
        wpaObj.forgetNetwork(self.testvars['wifi']['PSK']['ssid'])