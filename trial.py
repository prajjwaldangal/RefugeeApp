from bs4 import BeautifulSoup
st  = "[<button aria-expanded="false" aria-haspopup="true" aria-label="Sections Navigation &amp; Search" class="er09x8g1 css-l2ztic" data-testid="nav-button"><svg class="css-1fe7a5q" viewbox="0 0 16 16"><rect fill="#333333" height="2" width="14" x="1" y="3"></rect><rect fill="#333333" height="2" width="14" x="1" y="7"></rect><rect fill="#333333" height="2" width="14" x="1" y="11"></rect></svg></button>, <button aria-label="Sections Navigation" class="css-19lv58h er09x8g2" id="desktop-sections-button"><span class="css-vz7hjd">Sections</span><svg class="css-1fe7a5q" viewbox="0 0 16 16"><rect fill="#333333" height="2" width="14" x="1" y="3"></rect><rect fill="#333333" height="2" width="14" x="1" y="7"></rect><rect fill="#333333" height="2" width="14" x="1" y="11"></rect></svg></button>, <button class="css-mgtjo2 ewfai8r0" data-test-id="search-button"><span class="css-vz7hjd">SEARCH</span><svg class="css-1fe7a5q" viewbox="0 0 16 16"><path d="M11.3,9.2C11.7,8.4,12,7.5,12,6.5C12,3.5,9.5,1,6.5,1S1,3.5,1,6.5S3.5,12,6.5,12c1,0,1.9-0.3,2.7-0.7l3.3,3.3c0.3,0.3,0.7,0.4,1.1,0.4s0.8-0.1,1.1-0.4c0.6-0.6,0.6-1.5,0-2.1L11.3,9.2zM6.5,10.3c-2.1,0-3.8-1.7-3.8-3.8c0-2.1,1.7-3.8,3.8-3.8c2.1,0,3.8,1.7,3.8,3.8C10.3,8.6,8.6,10.3,6.5,10.3z" fill="#333"></path></svg></button>, <button class="css-1bnxwmn ez4a0qj0">Subscribe</button>, <button class="css-1bnxwmn ez4a0qj0" data-testid="login-button">Log In</button>, <button aria-expanded="false" aria-haspopup="true" aria-label="User Settings" class="ez4a0qj4 css-1i8g3m4" data-testid="user-settings-button"><svg class="css-10m9xeu" fill="#333" viewbox="0 0 16 16"><path d="M8,10c-2.5,0-7,1.1-7,3.5V16h14v-2.5C15,11.1,10.5,10,8,10z"></path><circle cx="8" cy="4" r="4"></circle></svg></button>, <button aria-label="Sections" class="css-1k9ek97" data-testid="mini-nav-sections-button"><svg class="css-1hd1ne6" viewbox="0 0 16 16"><rect fill="#333333" height="2" width="14" x="1" y="3"></rect><rect fill="#333333" height="2" width="14" x="1" y="7"></rect><rect fill="#333333" height="2" width="14" x="1" y="11"></rect></svg></button>, <button class="css-1vv8nt6" type="button"><svg class="css-2ejkui" stroke="#fff" stroke-linecap="round" stroke-width="1" style="opacity:0.95" viewbox="0 0 12 12"><line x1="11" x2="1" y1="1" y2="11"></line><line x1="1" x2="11" y1="1" y2="11"></line></svg></button>]"
print("earch" in st)