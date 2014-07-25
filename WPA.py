from marionette.by import By
from gaiatest.apps.base import Base
import time

class WpaEap(Base):
    def selectWPANetwork(self,networkName):
        # select WPA-EAP network from available networks        
        this_network_locator = ('xpath', "//li/a[text()='%s']" % networkName)        
        self.wait_for_element_displayed(*this_network_locator)
        display_item = self.marionette.find_element(*this_network_locator)
        self.marionette.execute_script("arguments[0].scrollIntoView(false);", [display_item])
        display_item.tap()
        
    def selectEAPMethod(self,eapName):
        # locate eap first        
        _select_eap_locator = (By.CSS_SELECTOR, 'span[class="button icon icon-dialog"]')
        self.wait_for_element_displayed(*_select_eap_locator)        
        display_item = self.marionette.find_element(*_select_eap_locator)
        self.marionette.execute_script("arguments[0].scrollIntoView(false);", [display_item])
        display_item.tap()
        
        #switch to frame
        self.marionette.switch_to_frame()
        
        self.selectOptions(eapName)
       
        self.apps.switch_to_displayed_app()   
        
    def choosePhase2Auth(self,method):            
        _select_phase_2_auth = (By.CSS_SELECTOR, 'p[data-l10n-id="auth-phase2"]+span[class="button icon icon-dialog"]')
        self.wait_for_element_displayed(*_select_phase_2_auth)
        self.marionette.find_element(*_select_phase_2_auth).tap()        
        
        self.marionette.switch_to_frame()
        
        self.selectOptions(method)
        
        self.apps.switch_to_displayed_app()           
    
    def inputIdentity(self,identityName):
        #input identity        
        _identity_input_locator = (By.CSS_SELECTOR, '#wifi-auth input[type="text"]')
        identity_field = self.marionette.find_element(*_identity_input_locator)
        identity_field.send_keys(identityName)   
        
    def inputPassword(self,password):
        #input password        
        _password_input_locator = (By.CSS_SELECTOR, 'li[class="password"] input[type="password"]')
        self.wait_for_element_displayed(*_password_input_locator)
        password_field = self.marionette.find_element(*_password_input_locator)
        password_field.send_keys(password)
        
    def join(self):
        ok_locator = (By.CSS_SELECTOR, 'span[data-l10n-id="ok"]')
        self.wait_for_element_displayed(*ok_locator)
        ok_locator_element = self.marionette.find_element(*ok_locator)
        ok_locator_element.tap()
        
        time.sleep(6)
        
    def getActiveNetworkName(self):        
        _connected_message_locator_network = (By.CSS_SELECTOR, '#wifi-availableNetworks li.active a')
        activeNetwork=''
        try:            
            self.wait_for_element_displayed(*_connected_message_locator_network)
            _connected_network_name = self.marionette.find_element(*_connected_message_locator_network)
            activeNetwork =  _connected_network_name.text
        except Exception:
            activeNetwork = 'None'
            
        return activeNetwork
        
    
    def getActiveNetworkStatus(self):
        activeNetworkStatus = ''
        try:
            _connected_message_locator = (By.CSS_SELECTOR, '#wifi-availableNetworks li.active small')
            self.wait_for_element_displayed(*_connected_message_locator)
            _connected_network_status = self.marionette.find_element(*_connected_message_locator)
            activeNetworkStatus = _connected_network_status.text
        except Exception:            
            activeNetworkStatus = 'N/A'
        
        return activeNetworkStatus
        
    def selectServerCertificate(self, certName):        
        _server_cert_locator = (By.CSS_SELECTOR, 'p[data-l10n-id="server-certificate"]+span[class="button icon icon-dialog"]')
        self.wait_for_element_displayed(*_server_cert_locator)
        self.marionette.find_element(*_server_cert_locator).tap()        
               
        self.marionette.switch_to_frame()
        
        self.selectOptions(certName)
        
        self.apps.switch_to_displayed_app()   
        
    def getStatusSecurityMethod(self):
        _connected_network_locator = (By.CSS_SELECTOR, '#wifi-availableNetworks li.active a')
        self.wait_for_element_displayed(*_connected_network_locator)
        self.marionette.find_element(*_connected_network_locator).tap()
        
        _security_method_locator = (By.CSS_SELECTOR, 'span[data-security=""]')
        self.wait_for_element_displayed(*_security_method_locator)
        security_method = self.marionette.find_element(*_security_method_locator).text
        
        _back_locator = (By.CSS_SELECTOR, '#wifi-status button[type="reset"]')
        self.wait_for_element_displayed(*_back_locator)        
        _back_button = self.marionette.find_element(*_back_locator)
        _back_button.tap()
        self.wait_for_element_displayed(*_connected_network_locator)
        
        return security_method
    
    def getStatusSignalStrengh(self):
        _connected_network_locator = (By.CSS_SELECTOR, '#wifi-availableNetworks li.active a')
        self.wait_for_element_displayed(*_connected_network_locator)
        self.marionette.find_element(*_connected_network_locator).tap()
        
        _data_signal_locator = (By.CSS_SELECTOR, 'span[data-signal=""]')
        self.wait_for_element_displayed(*_data_signal_locator)
        data_signal = self.marionette.find_element(*_data_signal_locator).text
        
        _back_locator = (By.CSS_SELECTOR, '#wifi-status button[type="reset"]')
        self.wait_for_element_displayed(*_back_locator)        
        _back_button = self.marionette.find_element(*_back_locator)
        _back_button.tap()
        self.wait_for_element_displayed(*_connected_network_locator)
        
        return data_signal
    
    def getStatusIP(self):
        _connected_network_locator = (By.CSS_SELECTOR, '#wifi-availableNetworks li.active a')
        self.wait_for_element_displayed(*_connected_network_locator)
        self.marionette.find_element(*_connected_network_locator).tap()
        
        _ip_locator = (By.CSS_SELECTOR, 'span[data-ip=""]')
        self.wait_for_element_displayed(*_ip_locator)
        ip_address = self.marionette.find_element(*_ip_locator).text
        
        _back_locator = (By.CSS_SELECTOR, '#wifi-status button[type="reset"]')
        self.wait_for_element_displayed(*_back_locator)        
        _back_button = self.marionette.find_element(*_back_locator)
        _back_button.tap()
        self.wait_for_element_displayed(*_connected_network_locator)
        
        return ip_address
    
    def getStatusSpeed(self):
        _connected_network_locator = (By.CSS_SELECTOR, '#wifi-availableNetworks li.active a')
        self.wait_for_element_displayed(*_connected_network_locator)
        self.marionette.find_element(*_connected_network_locator).tap()
        
        _speed_locator = (By.CSS_SELECTOR, 'span[data-speed=""]')
        self.wait_for_element_displayed(*_speed_locator)
        link_speed = self.marionette.find_element(*_speed_locator).text
        
        _back_locator = (By.CSS_SELECTOR, '#wifi-status button[type="reset"]')
        self.wait_for_element_displayed(*_back_locator)        
        _back_button = self.marionette.find_element(*_back_locator)
        _back_button.tap()
        self.wait_for_element_displayed(*_connected_network_locator)
        
        return link_speed
    
    def forgetNetwork(self,networkName):
        #forget wifi network
        _connected_network_locator = (By.CSS_SELECTOR, '#wifi-availableNetworks li.active a')
        self.wait_for_element_displayed(*_connected_network_locator)
        self.marionette.find_element(*_connected_network_locator).tap()
        
        _forget_network_locator = (By.CSS_SELECTOR, 'span[data-l10n-id="forget"]')
        self.wait_for_element_displayed(*_forget_network_locator)
        _forget_button = self.marionette.find_element(*_forget_network_locator)
        _forget_button.tap()
        
        this_network_locator = ('xpath', "//li/a[text()='%s']" % networkName)        
        self.wait_for_element_displayed(*this_network_locator)
        display_item = self.marionette.find_element(*this_network_locator)
        self.marionette.execute_script("arguments[0].scrollIntoView(false);", [display_item])
        
    def selectOptions(self,optionName):
        options = self.marionette.find_elements(By.CSS_SELECTOR, '#value-selector-container li')
        
        certTap = False
        for li in options:
            if li.text == '%s' % optionName:
                li.tap()
                certTap = True
                break
        if certTap == False:
            errorMsg = '\"' + optionName + '\" is not found.'
            raise Exception(errorMsg)
        
        #click OK
        _ok_select_auth = (By.CSS_SELECTOR, 'button.value-option-confirm')
        self.wait_for_element_displayed(*_ok_select_auth)
        self.marionette.find_element(*_ok_select_auth).tap()

class SrvCertOp(Base):
    def importSrvCert(self,name):
        #tap manage certificate button
        certframe = self.marionette.get_active_frame()
        
        mng_cert_locator = (By.CSS_SELECTOR, '#manageCertificates')
        self.wait_for_element_displayed(*mng_cert_locator)        
        self.marionette.find_element(*mng_cert_locator).tap()        
        
        #tap import certificate button
        imp_cert_locator = (By.CSS_SELECTOR, '#importCertificate')
        self.wait_for_element_displayed(*imp_cert_locator)        
        self.marionette.find_element(*imp_cert_locator).tap()        
        
        #select 1st item from the list
        cert_item_locator = ('xpath', "//li/a[text()='%s']" % name)
        self.wait_for_element_displayed(*cert_item_locator)        
        self.marionette.find_element(*cert_item_locator).tap()
        
        #click done for importing        
        _cert_done_locator = (By.CSS_SELECTOR, 'span[data-l10n-id="done"]')
        self.wait_for_element_displayed(*_cert_done_locator)        
        self.marionette.find_element(*_cert_done_locator).tap()
        
        time.sleep(2)        
                       
        self.marionette.switch_to_frame()
        self.marionette.switch_to_frame(certframe)
        
        #choose certificate 
        #_cert_item_checkbox_locator = ('xpath', "//ul/li/label/span[text()='%s']" % name)
        #self.wait_for_element_displayed(*_cert_item_checkbox_locator)
        #self.marionette.find_element(*_cert_item_checkbox_locator)
        
        #go back to wifi settings
        #_back_locator = (By.CSS_SELECTOR, '#wifi-manageCertificates span[data-l10n-id="back"]')
        _back_locator = (By.CSS_SELECTOR, '#wifi-manageCertificates button[type="reset"]')
        self.wait_for_element_displayed(*_back_locator)        
        _back_button = self.marionette.find_element(*_back_locator)
        _back_button.tap()

        
    def deleteSrvCert(self,name):
                
        #tap manage certificate button
        mng_cert_locator = (By.CSS_SELECTOR, '#manageCertificates')
        self.wait_for_element_displayed(*mng_cert_locator)        
        self.marionette.find_element(*mng_cert_locator).tap()        
        
        #choose certificate 
        _cert_item_checkbox_locator = ('xpath', "//ul/li/label/span[text()='%s']" % name)
        self.wait_for_element_displayed(*_cert_item_checkbox_locator)
        self.marionette.find_element(*_cert_item_checkbox_locator).tap()        
        
        #click delete button
        _del_cert_locator = (By.CSS_SELECTOR, '#deleteCertificate')
        self.wait_for_element_displayed(*_del_cert_locator)
        self.marionette.find_element(*_del_cert_locator).tap()        
        
        #go back to wifi settings
        _back_locator = (By.CSS_SELECTOR, '#wifi-manageCertificates span[data-l10n-id="back"]')
        self.wait_for_element_displayed(*_back_locator)        
        _back_button = self.marionette.find_element(*_back_locator)
        _back_button.tap()
        