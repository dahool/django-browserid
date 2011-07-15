# -*- coding: utf-8 -*-
'''/
Copyright (c) 2011, Sergio Gabriel Teves
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation and/or other materials
  provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS
OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT 
OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import httplib
import urllib
import json
import time

class InvalidAssertionException(Exception):
    pass
    
class BrowserID:
    
    _email = None
    _audience = None
    _validUntil = None
    _issuer = None
    
    def __init__(self, email, audience, validUntil, issuer)
        self._email = email
        self._audience = audience
        self._validUntil = validUntil
        self._issuer = issuer
        
    def _get_email(self):
        return self._email
    email = property(_get_email)

    def _get_audience(self):
        return self._audience
    audience = property(_get_audience)
    
    def _get_validUntil(self):
        return self._validUntil
    validUntil = property(_get_validUntil)
    
    def _get_issuer(self):
        return self._issuer
    issuer = property(_get_issuer)
                    
class BrowserIDHelper:
    '''/
    Helper for BrowserId Assertion Validation
    '''
    
    _host = 'browserid.org'
    _url = '/verify?assertion=%(assertion)s&audience=%(audience)s'

    def validate(assertion, hostname):
        conn = httplib.HTTPSConnection(self._host)
        conn.request("GET", self._url % {'assertion': assertion, 'audience': hostname})
        res = conn.getresponse()
        if res.status == httplib.OK:
            data = res.read()
            d = json.loads(data)
            if d['status'] == 'failure':
                raise InvalidAssertionException(d['reason'])
            elif d['status'] == 'okay':
                expires = time.gmtime(d['valid-until']/1000)
                if expires < time.gmtime():
                    raise InvalidAssertionException('Assertion is expired')
                b = BrowserID(d['email'],d['audience'],expires, d['issuer'])
        else:
            raise InvalidAssertionException(res.reason)
        conn.close()
        return b
            
