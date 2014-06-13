from marionette.by import By
from gaiatest.apps.base import Base
import time

class WpaEap(Base):
    def selectWPANetwork(self,networkName):
        # select WPA-EAP network from available networks        
        this_network_locator = ('xpath', "//li/a[text()='%s']" % networkName)
        preferedNetwork = self.wait_for_element_present(*this_network_locator)
        preferedNetwork.tap()
        
    def selectEAPMethod(self,eapName):
        # locate eap first
        _select_eap_locator = (By.CSS_SELECTOR, 'span[class="button icon icon-dialog"]')
        self.wait_for_element_displayed(*_select_eap_locator)
        self.wait_for_element_present(*_select_eap_locator).tap()
        
        #switch to frame
        self.marionette.switch_to_frame()
        
        #select EAP
        options = self.marionette.find_elements(By.CSS_SELECTOR, '#value-selector-container li')
        
        for li in options:
            if li.text == '%s' % eapName:
                li.tap()
                break
        
        #click OK
        _ok_select_eap = (By.CSS_SELECTOR, 'button.value-option-confirm')
        _ok_button_eap = self.wait_for_element_present(*_ok_select_eap)        
        _ok_button_eap.tap()
        
        self.apps.switch_to_displayed_app()   
        
    def choosePhase2Auth(self,method):
        #import pdb; pdb.set_trace()
        _select_phase_2_auth = (By.CSS_SELECTOR, 'p[data-l10n-id="auth-phase2"]+span[class="button icon icon-dialog"]')
        self.wait_for_element_displayed(*_select_phase_2_auth)
        self.wait_for_element_present(*_select_phase_2_auth).tap()
        
        self.marionette.switch_to_frame()
        
        options = self.marionette.find_elements(By.CSS_SELECTOR, '#value-selector-container li')
        
        for li in options:
            if li.text == '%s' % method:
                li.tap()
                break
        
        #click OK
        _ok_select_auth = (By.CSS_SELECTOR, 'button.value-option-confirm')
        _ok_button_eap = self.wait_for_element_present(*_ok_select_auth)        
        _ok_button_eap.tap()
        
        self.apps.switch_to_displayed_app()   
        
    
    def inputIdentity(self,identityName):
        #input identity        
        _identity_input_locator = (By.CSS_SELECTOR, '#wifi-auth input[type="text"]')
        identity_field = self.marionette.find_element(*_identity_input_locator)
        identity_field.send_keys(identityName)   
        
    def inputPassword(self,password):
        #input password        
        _password_input_locator = (By.CSS_SELECTOR, '#wifi-auth input[type="password"]')
        password_field = self.marionette.find_element(*_password_input_locator)
        password_field.send_keys(password)
        
    def join(self):
        ok_locator = (By.CSS_SELECTOR, 'span[data-l10n-id="ok"]')
        ok_button = self.wait_for_element_present(*ok_locator)
        ok_button.tap()
        
        time.sleep(3)
        
    def getActiveNetworkName(self):
        #import pdb;pdb.set_trace()
        _connected_message_locator_network = (By.CSS_SELECTOR, '#wifi-availableNetworks li.active a')
        activeNetwork=''
        try:
            self.wait_for_element_present(*_connected_message_locator_network)
            _connected_network_name = self.marionette.find_element(*_connected_message_locator_network)
            activeNetwork =  _connected_network_name.text
        except Exception:
            activeNetwork = 'None'
            
        return activeNetwork
        
    
    def getActiveNetworkStatus(self):
        activeNetworkStatus = ''
        try:
            _connected_message_locator = (By.CSS_SELECTOR, '#wifi-availableNetworks li.active small')
            _connected_network_status = self.marionette.find_element(*_connected_message_locator)
            activeNetworkStatus = _connected_network_status.text
        except Exception:            
            activeNetworkStatus = 'N/A'
                
        return activeNetworkStatus
        
    def forgetNetwork(self,networkName):
        #forget wifi network
        _connected_network_locator = (By.CSS_SELECTOR, '#wifi-availableNetworks li.active a')
        self.wait_for_element_present(*_connected_network_locator)
        self.marionette.find_element(*_connected_network_locator).tap()
        
        _forget_network_locator = (By.CSS_SELECTOR, 'span[data-l10n-id="forget"]')
        self.wait_for_element_displayed(*_forget_network_locator)
        self.wait_for_element_present(*_forget_network_locator).tap()
    