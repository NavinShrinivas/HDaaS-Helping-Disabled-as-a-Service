# HDaaS-Helping-Disabled-as-a-Service
<h1>INTRO:</h1>
<p>Service having multiple Sub-Service with the sole aim of helping the disabled with use or electronics and robotics</p>
<p>Domains our projects falls under :
	<ol>
		<li>engineering (using basic physics  and math for one Sub-Service) </li>
		<li>web development (flask , api’s by google) </li>
		<li>Robotics (not implemented for hackathon) </li>
		<li>electronics (sensors and such not implemented)</li>
	</ol>
</p>
<hr>
<h1>SERVICES AND HOW TO USE EM : </h1>
<h2>Tippoff service </h2>
<p>a person in wheelchair may not realise when a slope may not be safe to use, and sometimes unfortunately they may fall off
worry not our project aims to help these people in situations as such mentioned, there will be three beeps when the wheelchair tries to travel a slope it cant hence avoiding a unfortuate accident</p
<p>
	<ul>
        <li><p>This service is to be used to detect if a slope is safe to climb over </p></li>
        <li><p>service call format : <code>http://locahost:5000/tippoffservice/x/y/typ </code></p></li>
        <li><p>OPTIONS : 
            <ul>
                <li>x : height between flat floor and sensor [can be hard coded]</li>
                <li>y : data recived from sensor of distance between sensor and slope</li>
                <li>type :
                    <ol>
                        <li>wa : without assistance saftey tolerances of ADA standards will be taken into account</li>
                        <li>a : assisted saftey tolerances of ADA standards will be taken into account</li>
                    </ol>
                </li>
            </ul>
        </ul>
<h2>TextToBraille</h2>
<p>this converts the text to braille format considering a mechnical solutiion by desing a device with mechnical brailles</p>
<p>service call format : <code>http://localhost:5000/txt-braille/txt </code></p>
<p>This returns a list with each elements of strings of length 6 each charecter either 1 or 0. The index of the number corresponds to a particular posistion on 3X6 Braille matrix</p>
<hr>
<h1>FUTURE TO ADD SUB-SERIVCES</h1>
<ul>
	<li>TTSService real time text to speech service</li>
</ul>
