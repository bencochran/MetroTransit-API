#!/usr/bin/env python
#
# MetroTransit API
# Corey Maul (chmaul AT gmail DOT com)
#
# Copyright (c) 2009 Corey Maul
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import wsgiref.handlers


from google.appengine.ext import webapp


class MainHandler(webapp.RequestHandler):

  def get(self):
    defaultHtml = '''<html>
	<body>
    <h1 id="metro_transit_api">Metro Transit API</h1>

    <p>This API provides data from MetroTransit.org in a JSON encoded format.</p>

    <p>Currently Supported Interfaces:</p>

    <ul>
    <li>routes - Displays the list of all routes provided by MetroTransit.</li>
    <li>direction - Displays the list of potential directions for a given route.</li>
    <li>stops - Displays the list of stops given a route and a direction</li>
    <li>nextrip - Displays a list of times for the bus to arrive given a stop,
    direction, and route</li>
    </ul>

    <h2 id="routes">Routes</h2>

    <p>Example: <em>http://metrotransitapi.appspot.com/routes</em></p>

    <h3 id="sample_output">Sample output:</h3>

    <pre><code>[{"name": "55 - Hiawatha Light Rail", "number": 55}, {"name": "888 - Northstar Commuter Rail", "number": 888}, {"name": "2 - Franklin Av - Riverside Av - U of M - 8th St SE", "number": 2}, {"name": "3 - U of M - Como Av - Energy Park Dr - Maryland Av", "number": 3}, {"name": "4 - New Brighton - Johnson St - Bryant Av - Southtown", "number": 4}, {"name": "5 - Brklyn Center - Fremont - 26th Av - Chicago - MOA", "number": 5}, {"name": "6 - U of M - Hennepin - Xerxes - France - Southdale", "number": 6}, ... ]
    </code></pre>

    <h2 id="direction">Direction</h2>

    <p>Example: <em>http://metrotransitapi.appspot.com/direction?route=4</em></p>

    <h3 id="required_parameters">Required parameters:</h3>

    <ul>
    <li>route</li>
    </ul>

    <h3 id="sample_output">Sample output:</h3>

    <pre><code>[{"code": 4, "name": "NORTHBOUND"}, {"code": 1, "name": "SOUTHBOUND"}]
    </code></pre>

    <h2 id="stops">Stops</h2>

    <p>Example: <em>http://metrotransitapi.appspot.com/stops?route=6&amp;direction=1</em></p>

    <h3 id="required_parameters">Required parameters:</h3>

    <ul>
    <li>route</li>
    <li>direction</li>
    </ul>

    <h3 id="sample_output">Sample output:</h3>

    <pre><code>[{"code": "OAWA", "name": "Oak St SE and Washington Ave SE"}, {"code": "4S15", "name": "4th St SE and 15th Ave SE"}, {"code": "4SCE", "name": "4th St SE and Central Ave SE"}, {"code": "1S1A", "name": "1st Ave N and 1st St"}, {"code": "7SNI", "name": "Nicollet Mall and 7th St S"}, {"code": "8SHE", "name": "Hennepin Ave and 8th St"}, ... ]
    </code></pre>

    <h2 id="nextrip">Nextrip</h2>

    <p>Example: <em>http://metrotransitapi.appspot.com/nextrip?route=6&amp;direction=1&amp;stop=HEUP</em></p>

    <h3 id="required_parameters">Required parameters:</h3>

    <ul>
    <li>route</li>
    <li>direction</li>
    <li>stop</li>
    </ul>

    <h3 id="sample_output">Sample output:</h3>

    <pre><code>[{"time": "9 Min", "actual": true, "number": "6B", "name": "France Av \/Southdale \/ Via Woodale"}, {"time": "7:50", "actual": false, "number": "6E", "name": "Minn Drive \/ Xerxes Av \/ Southdale"}, {"time": "8:05", "actual": false, "number": "6D", "name": "Southdale\/France Av"}, {"time": "8:18", "actual": false, "number": "6E", "name": "Minn Drive \/ Xerxes Av \/ Southdale"}, {"time": "8:32", "actual": false, "number": "6B", "name": "France Av \/Southdale \/ Via Woodale"}, {"time": "8:47", "actual": false, "number": "6E", "name": "Minn Drive \/ Xerxes Av \/ Southdale"}]
    </code></pre>

    <h2 id="info_license">Info &amp; License</h2>

    <p>Developed by Corey Maul. Very loosely based on yourmuni by mihaysa (http://yourmuni.appspot.com)</p>

    <p>Full source code is available at: http://www.github.com/cmaul/ </p>

    <p>Copyright (c) 2009 Corey Maul</p>

    <p>Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the &#8220;Software&#8221;), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:</p>

    <p>The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.</p>

    <p>THE SOFTWARE IS PROVIDED &#8220;AS IS&#8221;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.</p>
	</body>
</html>'''

    self.response.out.write(defaultHtml)


def main():
  application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
