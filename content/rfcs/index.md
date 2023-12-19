---
title: DNS RFC Repository
date: 2023-12-19
---

We maintain an up-to-date repository of DNS-related RFCs. 
To help quickly gather and browse documents of interest, we also give finer-grained labels under particular topics (e.g., DNSSEC, IDNA, DNS privacy) to each RFC.

This repository is expected to be updated once a month. 
It now comprises **<span id="rfcsnumber">42</span>** RFCs under **<span
	id="labelsnumber">42</span>** labels, including:

- Documents subsequent to RFC 882
- DNS specification: namespace, name registration, DNS protocol
- DNS operation: functionalities and recommendations about running DNS services
- DNS security: security extensions, threat analysis, and proposed solutions
- DNS application: Internet functionalities that explicitly rely on the DNS (e.g., SPF, DANE)
- Obsoleted/deprecated versions of the above


Comments or suggestions are extremely welcome! 
[Contact us](mailto:luchaoyi@tsinghua.edu.cn) if you find an RFC missing, mis-labeled, should be removed, or for any other feedback.


<body>
	<!-- <table id="checkbutton" style="border-top: 0px;"></table> -->
	<table id="checkboxes" style="border-collapse: collapse;">
		<tr>
			<th colspan="8" style="vertical-align: middle; text-align: center;">RFC status
				<button class="btn btn-outline-primary btn-page-header" id="rfc_status_s">Select All </button>
				<button class="btn btn-outline-primary btn-page-header" id="rfc_status_uns">Clear All</button>
			</th>
		</tr>
	</table>
	<table id="checkboxes_topics" style="border-collapse: collapse;">
		<tr style="line-height: 2;">
			<th colspan="6" style="vertical-align: middle; text-align: center;">Topics <button
					class="btn btn-outline-primary btn-page-header" id="topic_s">Select All</button><button
					class="btn btn-outline-primary btn-page-header" id="topic_uns">Clear All</button>
			</th>
		</tr>
		</tr>
	</table>
	<br>
	<button class="btn btn-outline-primary btn-page-header"><strong><span id="rfcshowed">42</span></strong> rfcs shown</button>
	<br>
	<table id=myTable>	<tr>
		<td><strong>﻿RFC status</strong></td>
		<td><strong>Topic 1</strong></td>
		<td><strong>Topic 2</strong></td>
		<td><strong>RFC</strong></td>
		<td><strong>Title</strong></td>
		<td><strong>Obsoleted by</strong></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>PKI Application</td>
		<td>SRV/SVCB Functionalities</td>
		<td><a href="https://www.rfc-editor.org/info/rfc9525">9525</a></td>
		<td>Service Identity in TLS</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Filtering</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9505">9505</a></td>
		<td>A Survey of Worldwide Censorship Techniques</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Servicing</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9498">9498</a></td>
		<td>The GNU Name System</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9476">9476</a></td>
		<td>The .alt Special-Use Top-Level Domain</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Servicing</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc9471">9471</a></td>
		<td>DNS Glue Requirements in Referral Responses</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Encrypted DNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9464">9464</a></td>
		<td>Internet Key Exchange Protocol Version 2 (IKEv2) Configuration for Encrypted DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Encrypted DNS</td>
		<td>SRV/SVCB Functionalities</td>
		<td><a href="https://www.rfc-editor.org/info/rfc9462">9462</a></td>
		<td>Discovery of Designated Resolvers</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>SRV/SVCB Functionalities</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9461">9461</a></td>
		<td>Service Binding Mapping for DNS Servers</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>SRV/SVCB Functionalities</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9460">9460</a></td>
		<td>Service Binding and Parameter Specification via the DNS (SVCB and HTTPS Resource Records)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNS Privacy</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9446">9446</a></td>
		<td>Reflections on Ten Years Past the Snowden Revelations</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>PKI Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9444">9444</a></td>
		<td>Automated Certificate Management Environment (ACME) for Subdomains</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Zone Transfer/Update</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9432">9432</a></td>
		<td>DNS Catalog Zones</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>DNSSEC - General Operation</td>
		<td>Clarification/Terminology</td>
		<td><a href="https://www.rfc-editor.org/info/rfc9364">9364</a></td>
		<td>DNS Security Extensions (DNSSEC)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9361">9361</a></td>
		<td>ICANN Trademark Clearinghouse (TMCH) Functional Specifications</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc9276">9276</a></td>
		<td>Guidance for NSEC3 Parameter Settings </td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Threats/Vulnerabilities & Patches</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9267">9267</a></td>
		<td>Common Implementation Anti-Patterns Related to Domain Name System (DNS) Resource Record (RR) Processing</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Encrypted DNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9250">9250</a></td>
		<td>DNS over Dedicated QUIC Connections</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9233">9233</a></td>
		<td>Internationalized Domain Names for Applications 2008 (IDNA2008) and Unicode 12.0.0</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>Encrypted DNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9230">9230</a></td>
		<td>Oblivious DNS over HTTPS</td>
		<td></td>
	</tr>
	<tr>
		<td>Internet Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9224">9224</a></td>
		<td>Finding the Authoritative Registration Data Access Protocol (RDAP) Service</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>DNS over TCP</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc9210">9210</a></td>
		<td>DNS Transport over TCP - Operational Requirements</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Servicing</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc9199">9199</a></td>
		<td>Considerations for Large Authoritative DNS Server Operators</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9167">9167</a></td>
		<td>Registry Maintenance Notification for the Extensible Provisioning Protocol (EPP)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Problem Statement</td>
		<td>Clarification/Terminology</td>
		<td><a href="https://www.rfc-editor.org/info/rfc9157">9157</a></td>
		<td>Revised IANA Considerations for DNSSEC</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNS Privacy</td>
		<td>Servicing</td>
		<td><a href="https://www.rfc-editor.org/info/rfc9156">9156</a></td>
		<td>DNS Query Name Minimisation to Improve Privacy</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9154">9154</a></td>
		<td>Extensible Provisioning Protocol (EPP) Secure Authorization Information for Transfer</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9121">9121</a></td>
		<td>Deprecating Infrastructure "int" Domains</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Reverse DNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9120">9120</a></td>
		<td>Nameservers for the Address and Routing Parameter Area ("arpa") Domain</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>New RRs/Codes</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9108">9108</a></td>
		<td>YANG Types for DNS Classes and Resource Record Types</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Encrypted DNS</td>
		<td>Zone Transfer/Update</td>
		<td><a href="https://www.rfc-editor.org/info/rfc9103">9103</a></td>
		<td>DNS Zone Transfer over TLS</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>DNSSEC - Others</td>
		<td>PKI Application</td>
		<td><a href="https://www.rfc-editor.org/info/rfc9102">9102</a></td>
		<td>TLS DNSSEC Chain Extension</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9095">9095</a></td>
		<td>Extensible Provisioning Protocol (EPP) Domain Name Mapping Extension for Strict Bundling Registration</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9091">9091</a></td>
		<td>Experimental Domain-Based Message Authentication, Reporting, and Conformance (DMARC) Extension for Public Suffix Domains</td>
		<td></td>
	</tr>
	<tr>
		<td>Internet Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9083">9083</a></td>
		<td>JSON Responses for the Registration Data Access Protocol (RDAP)</td>
		<td></td>
	</tr>
	<tr>
		<td>Internet Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9082">9082</a></td>
		<td>Registration Data Access Protocol (RDAP) Query Format</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - General Operation</td>
		<td>Servicing</td>
		<td><a href="https://www.rfc-editor.org/info/rfc9077">9077</a></td>
		<td>NSEC and NSEC3: TTLs and Aggressive Use</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNS Privacy</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9076">9076</a></td>
		<td>DNS Privacy Considerations</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9038">9038</a></td>
		<td>Extensible Provisioning Protocol (EPP) Unhandled Namespaces</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9022">9022</a></td>
		<td>Domain Name Registration Data (DNRD) Objects Mapping</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Transaction Authentication</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc9018">9018</a></td>
		<td>Interoperable Domain Name System (DNS) Server Cookies</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8982">8982</a></td>
		<td>Registration Data Access Protocol (RDAP) Partial Response</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8977">8977</a></td>
		<td>Registration Data Access Protocol (RDAP) Query Parameters for Result Sorting and Paging</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>New RRs/Codes</td>
		<td>DNS Root</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8976">8976</a></td>
		<td>Message Digest for DNS Zones</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8958">8958</a></td>
		<td>Updated Registration Rules for URI.ARPA</td>
		<td></td>
	</tr>
	<tr>
		<td>Internet Standard</td>
		<td>Transaction Authentication</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8945">8945</a></td>
		<td>Secret Key Transaction Authentication for DNS (TSIG)</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>DNS Privacy</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8932">8932</a></td>
		<td>Recommendations for DNS Privacy Service Operators</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Flaws/Errors & Reporting</td>
		<td>Servicing</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8914">8914</a></td>
		<td>Extended DNS Errors</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8909">8909</a></td>
		<td>Registry Data Escrow Specification</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Flaws/Errors & Reporting</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8906">8906</a></td>
		<td>A Common Operational Problem in DNS Servers: Failure to Communicate</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Email Application</td>
		<td>Filtering</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8904">8904</a></td>
		<td>DNS Whitelist (DNSWL) Email Authentication Method Extension</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNSSEC - General Operation</td>
		<td>Servicing</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8901">8901</a></td>
		<td>Multi-Signer DNSSEC Models</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Threats/Vulnerabilities & Patches</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8900">8900</a></td>
		<td>IP Fragmentation Considered Fragile</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Service Discovery/mDNS</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8882">8882</a></td>
		<td>DNS-Based Service Discovery (DNS-SD) Privacy and Security Requirements</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Reverse DNS</td>
		<td>Namespace</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8880">8880</a></td>
		<td>Special Use Domain Name 'ipv4only.arpa'</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8807">8807</a></td>
		<td>Login Security Extension for the Extensible Provisioning Protocol (EPP)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNS Root</td>
		<td>Servicing</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8806">8806</a></td>
		<td>Running a Root Server Local to a Resolver</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Reverse DNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8777">8777</a></td>
		<td>DNS Reverse IP Automatic Multicast Tunneling (AMT) Discovery</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Servicing</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8767">8767</a></td>
		<td>Serving Stale Data to Improve DNS Resiliency</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Service Discovery/mDNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8766">8766</a></td>
		<td>Discovery Proxy for Multicast DNS-Based Service Discovery</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Zone Transfer/Update</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8765">8765</a></td>
		<td>DNS Push Notifications</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Zone Transfer/Update</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8764">8764</a></td>
		<td>Apple's DNS Long-Lived Queries Protocol</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8753">8753</a></td>
		<td>Internationalized Domain Names for Applications (IDNA) Review for New Unicode Versions</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Statement of Retirement</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8749">8749</a></td>
		<td>Moving DNSSEC Lookaside Validation (DLV) to Historic Status</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8748">8748</a></td>
		<td>Registry Fee Extension for the Extensible Provisioning Protocol (EPP)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IPv6 Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8683">8683</a></td>
		<td>Additional Deployment Guidelines for NAT64/464XLAT in Operator and Enterprise Networks</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>PKI Application</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8659">8659</a></td>
		<td>DNS Certification Authority Authorization (CAA) Resource Record</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>PKI Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8657">8657</a></td>
		<td>Certification Authority Authorization (CAA) Record Extensions for Account URI and Automatic Certificate Management Environment (ACME) Method Binding</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8624">8624</a></td>
		<td>Algorithm Implementation Requirements and Usage Guidance for DNSSEC</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Data Collection & Representation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8618">8618</a></td>
		<td>Compacted-DNS (C-DNS): A Format for DNS Packet Capture</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Email Application</td>
		<td>IDNA/Globalization</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8616">8616</a></td>
		<td>Email Authentication for Internationalized Mail</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Other Applications</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8598">8598</a></td>
		<td>Split DNS Configuration for the Internet Key Exchange Protocol Version 2 (IKEv2)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8590">8590</a></td>
		<td>Change Poll Extension for the Extensible Provisioning Protocol (EPP)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>New RRs/Codes</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8567">8567</a></td>
		<td>Customer Management DNS Resource Records</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>PKI Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8555">8555</a></td>
		<td>Automatic Certificate Management Environment (ACME)</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Servicing</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8553">8553</a></td>
		<td>DNS Attrleaf Changes: Fixing Specifications That Use Underscored Node Names</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Servicing</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8552">8552</a></td>
		<td>Scoped Interpretation of DNS Resource Records through "Underscored" Naming of Attribute Leaves</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8544">8544</a></td>
		<td>Organization Extension for the Extensible Provisioning Protocol (EPP)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8543">8543</a></td>
		<td>Extensible Provisioning Protocol (EPP) Organization Mapping</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8521">8521</a></td>
		<td>Registration Data Access Protocol (RDAP) Object Tagging</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td>DNS Root</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8509">8509</a></td>
		<td>A Root Key Trust Anchor Sentinel for DNSSEC</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Reverse DNS</td>
		<td>IPv6 Application</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8501">8501</a></td>
		<td>Reverse DNS in IPv6 for Internet Service Providers</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Clarification/Terminology</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8499">8499</a></td>
		<td>DNS Terminology</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8495">8495</a></td>
		<td>Allocation Token Extension for the Extensible Provisioning Protocol (EPP)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>New RRs/Codes</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8490">8490</a></td>
		<td>DNS Stateful Operations</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Encrypted DNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8484">8484</a></td>
		<td>DNS Queries over HTTPS (DoH)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNS Root</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8483">8483</a></td>
		<td>Yeti DNS Testbed</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Threats/Vulnerabilities & Patches</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8482">8482</a></td>
		<td>Providing Minimal-Sized Responses to DNS Queries That Have QTYPE=ANY</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>EDNS & Extensions</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8467">8467</a></td>
		<td>Padding Policies for Extension Mechanisms for DNS (EDNS(0))</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8463">8463</a></td>
		<td>A New Cryptographic Signature Method for DomainKeys Identified Mail (DKIM)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Data Collection & Representation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8427">8427</a></td>
		<td>Representing DNS Messages in JSON</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Reverse DNS</td>
		<td>Namespace</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8375">8375</a></td>
		<td>Special-Use Domain 'home.arpa.'</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8334">8334</a></td>
		<td>Launch Phase Mapping for the Extensible Provisioning Protocol (EPP)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Servicing</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8324">8324</a></td>
		<td>DNS Privacy, Authorization, Special Uses, Encoding, Characters, Matching, and Root Structure: Time for Another Look?</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Encrypted DNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8310">8310</a></td>
		<td>Usage Profiles for DNS over TLS and DNS over DTLS</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8301">8301</a></td>
		<td>Cryptographic Algorithm and Key Usage Update to DomainKeys Identified Mail (DKIM)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8264">8264</a></td>
		<td>PRECIS Framework: Preparation, Enforcement, and Comparison of Internationalized Strings in Application Protocols</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Namespace</td>
		<td>Clarification/Terminology</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8244">8244</a></td>
		<td>Special-Use Domain Names Problem Statement</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Service Discovery/mDNS</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8222">8222</a></td>
		<td>Selecting Labels for Use with Conventional DNS and Other Resolution Systems in DNS-Based Service Discovery</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Servicing</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8198">8198</a></td>
		<td>Aggressive Use of DNSSEC-Validated Cache</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>PKI Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8162">8162</a></td>
		<td>Using Secure DNS to Associate Certificates with Domain Names for S/MIME</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8145">8145</a></td>
		<td>Signaling Trust Anchor Knowledge in DNS Security Extensions (DNSSEC)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNS Root</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8128">8128</a></td>
		<td>IETF Appointment Procedures for the ICANN Root Zone Evolution Review Committee</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Threats/Vulnerabilities & Patches</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8117">8117</a></td>
		<td>Current Hostname Practice Considered Harmful</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>DNS Root</td>
		<td>Servicing</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8109">8109</a></td>
		<td>Initializing a DNS Resolver with Priming Queries</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IPv6 Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8106">8106</a></td>
		<td>IPv6 Router Advertisement Options for DNS Configuration</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>Encrypted DNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8094">8094</a></td>
		<td>DNS over Datagram Transport Layer Security (DTLS)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8080">8080</a></td>
		<td>Edwards-Curve Digital Security Algorithm (EdDSA) for DNSSEC</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8078">8078</a></td>
		<td>Managing DS Records from the Parent via CDS/CDNSKEY</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8063">8063</a></td>
		<td>Key Relay Mapping for the Extensible Provisioning Protocol</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8056">8056</a></td>
		<td>Extensible Provisioning Protocol (EPP) and Registration Data Access Protocol (RDAP) Status Mapping</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>DNSSEC - General Operation</td>
		<td>Flaws/Errors & Reporting</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8027">8027</a></td>
		<td>DNSSEC Roadblock Avoidance</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Namespace</td>
		<td>Threats/Vulnerabilities & Patches</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8023">8023</a></td>
		<td>Report from the Workshop and Prize on Root Causes and Mitigation of Name Collisions</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Clarification/Terminology</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc8020">8020</a></td>
		<td>NXDOMAIN: There Really Is Nothing Underneath</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>New RRs/Codes</td>
		<td>Other Applications</td>
		<td><a href="https://www.rfc-editor.org/info/rfc8005">8005</a></td>
		<td>Host Identity Protocol (HIP) Domain Name System (DNS) Extension</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7960">7960</a></td>
		<td>Interoperability Issues between Domain-based Message Authentication, Reporting, and Conformance (DMARC) and Indirect Email Flows</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td>DNS Root</td>
		<td><a href="https://www.rfc-editor.org/info/rfc7958">7958</a></td>
		<td>DNSSEC Trust Anchor Publication for the Root Zone</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>PKI Application</td>
		<td>Email Application</td>
		<td><a href="https://www.rfc-editor.org/info/rfc7929">7929</a></td>
		<td>DNS-Based Authentication of Named Entities (DANE) Bindings for OpenPGP</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>EDNS & Extensions</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7901">7901</a></td>
		<td>CHAIN Query Requests in DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Transaction Authentication</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7873">7873</a></td>
		<td>Domain Name System (DNS) Cookies</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>EDNS & Extensions</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7871">7871</a></td>
		<td>Client Subnet in DNS Queries</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Encrypted DNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7858">7858</a></td>
		<td>Specification for DNS over Transport Layer Security (TLS)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>EDNS & Extensions</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7830">7830</a></td>
		<td>The EDNS(0) Padding Option</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>EDNS & Extensions</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7828">7828</a></td>
		<td>The edns-tcp-keepalive EDNS0 Option</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>PKI Application</td>
		<td>Email Application</td>
		<td><a href="https://www.rfc-editor.org/info/rfc7817">7817</a></td>
		<td>Updated Transport Layer Security (TLS) Server Identity Check Procedure for Email-Related Protocols</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>DNS Privacy</td>
		<td>Servicing</td>
		<td><a href="https://www.rfc-editor.org/info/rfc7816">7816</a></td>
		<td>DNS Query Name Minimisation to Improve Privacy</td>
		<td>9156</td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Reverse DNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7793">7793</a></td>
		<td>Adding 100.64.0.0/10 Prefixes to the IPv4 Locally-Served DNS Zones Registry</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNS over TCP</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7766">7766</a></td>
		<td>DNS Transport over TCP - Implementation Requirements</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Filtering</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc7754">7754</a></td>
		<td>Technical Considerations for Internet Service Blocking and Filtering</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Reverse DNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7745">7745</a></td>
		<td>XML Schemas for Reverse DNS Management</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>DNS Root</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc7720">7720</a></td>
		<td>DNS Root Name Service Protocol and Deployment Requirements</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Clarification/Terminology</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7719">7719</a></td>
		<td>DNS Terminology</td>
		<td>8499</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Other Applications</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7712">7712</a></td>
		<td>Domain Name Associations (DNA) in the Extensible Messaging and Presence Protocol (XMPP)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNS Root</td>
		<td>Servicing</td>
		<td><a href="https://www.rfc-editor.org/info/rfc7706">7706</a></td>
		<td>Decreasing Access Time to Root Servers by Running One on Loopback</td>
		<td>8806</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7686">7686</a></td>
		<td>The ".onion" Special-Use Domain Name</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>PKI Application</td>
		<td>SRV/SVCB Functionalities</td>
		<td><a href="https://www.rfc-editor.org/info/rfc7673">7673</a></td>
		<td>Using DNS-Based Authentication of Named Entities (DANE) TLSA Records with SRV Records</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>PKI Application</td>
		<td>Email Application</td>
		<td><a href="https://www.rfc-editor.org/info/rfc7672">7672</a></td>
		<td>SMTP Security via Opportunistic DNS-Based Authentication of Named Entities (DANE) Transport Layer Security (TLS)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>PKI Application</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc7671">7671</a></td>
		<td>The DNS-Based Authentication of Named Entities (DANE) Protocol: Updates and Operational Guidance</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7646">7646</a></td>
		<td>Definition and Use of DNSSEC Negative Trust Anchors</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNS Privacy</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7626">7626</a></td>
		<td>DNS Privacy Considerations</td>
		<td>9076</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7583">7583</a></td>
		<td>DNSSEC Key Rollover Timing Considerations</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7564">7564</a></td>
		<td>PRECIS Framework: Preparation, Enforcement, and Comparison of Internationalized Strings in Application Protocols</td>
		<td>8264</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Service Discovery/mDNS</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc7558">7558</a></td>
		<td>Requirements for Scalable DNS-Based Service Discovery (DNS-SD) / Multicast DNS (mDNS) Extensions</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>New RRs/Codes</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7553">7553</a></td>
		<td>The Uniform Resource Identifier (URI) DNS Resource Record</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Reverse DNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7535">7535</a></td>
		<td>AS112 Redirection Using DNAME</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Reverse DNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7534">7534</a></td>
		<td>AS112 Nameserver Operations</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7505">7505</a></td>
		<td>A "Null MX" No Service Resource Record for Domains That Accept No Mail</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7489">7489</a></td>
		<td>Domain-based Message Authentication, Reporting, and Conformance (DMARC)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7485">7485</a></td>
		<td>Inventory and Analysis of WHOIS Registration Objects</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7484">7484</a></td>
		<td>Finding the Authoritative Registration Data (RDAP) Service</td>
		<td>9224</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7483">7483</a></td>
		<td>JSON Responses for the Registration Data Access Protocol (RDAP)</td>
		<td>9083</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7482">7482</a></td>
		<td>Registration Data Access Protocol (RDAP) Query Format</td>
		<td>9082</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Other Applications</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7479">7479</a></td>
		<td>Using Ed25519 in SSHFP Resource Records</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Zone Transfer/Update</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7477">7477</a></td>
		<td>Child-to-Parent Synchronization in DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Other Applications</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7393">7393</a></td>
		<td>Using the Port Control Protocol (PCP) to Update Dynamic DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7344">7344</a></td>
		<td>Automating DNSSEC Delegation Trust Maintenance</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Other Applications</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7336">7336</a></td>
		<td>Framework for Content Distribution Network Interconnection (CDNI)</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>EDNS & Extensions</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7314">7314</a></td>
		<td>Extension Mechanisms for DNS (EDNS) EXPIRE Option</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Namespace</td>
		<td>Threats/Vulnerabilities & Patches</td>
		<td><a href="https://www.rfc-editor.org/info/rfc7304">7304</a></td>
		<td>A Method for Mitigating Namespace Collisions</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>PKI Application</td>
		<td>Clarification/Terminology</td>
		<td><a href="https://www.rfc-editor.org/info/rfc7218">7218</a></td>
		<td>Adding Acronyms to Simplify Conversations about DNS-Based Authentication of Named Entities (DANE)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Other Applications</td>
		<td>Reverse DNS</td>
		<td><a href="https://www.rfc-editor.org/info/rfc7216">7216</a></td>
		<td>Location Information Server (LIS) Discovery Using IP Addresses and Reverse DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Email Application</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc7208">7208</a></td>
		<td>Sender Policy Framework (SPF) for Authorizing Use of Domains in E-Mail, Version 1</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7129">7129</a></td>
		<td>Authenticated Denial of Existence in the DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNS Root</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7108">7108</a></td>
		<td>A Summary of Various Mechanisms Deployed at L-Root for the Identification of Anycast Nodes</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7085">7085</a></td>
		<td>Top-Level Domains That Are Already Dotless</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IPv6 Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7051">7051</a></td>
		<td>Analysis of Solution Proposals for Hosts to Learn NAT64 Prefix</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IPv6 Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc7050">7050</a></td>
		<td>Discovery of the IPv6 Prefix Used for IPv6 Address Synthesis</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>New RRs/Codes</td>
		<td>Other Applications</td>
		<td><a href="https://www.rfc-editor.org/info/rfc7043">7043</a></td>
		<td>Resource Records for EUI-48 and EUI-64 Addresses in the DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6975">6975</a></td>
		<td>Signaling Cryptographic Algorithm Understanding in DNS Security Extensions (DNSSEC)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Other Applications</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc6950">6950</a></td>
		<td>Architectural Considerations on Application Features in the DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6944">6944</a></td>
		<td>Applicability Statement: DNS Security (DNSSEC) DNSKEY Algorithm Implementation Status</td>
		<td>8624</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IDNA/Globalization</td>
		<td>Namespace</td>
		<td><a href="https://www.rfc-editor.org/info/rfc6927">6927</a></td>
		<td>Variants in Second-Level Names Registered in Top-Level Domains</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IDNA/Globalization</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc6912">6912</a></td>
		<td>Principles for Unicode Code Point Inclusion in Labels in the DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Clarification/Terminology</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6895">6895</a></td>
		<td>Domain Name System (DNS) IANA Considerations</td>
		<td></td>
	</tr>
	<tr>
		<td>Internet Standard</td>
		<td>EDNS & Extensions</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6891">6891</a></td>
		<td>Extension Mechanisms for DNS (EDNS(0))</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>PKI Application</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc6844">6844</a></td>
		<td>DNS Certification Authority Authorization (CAA) Resource Record</td>
		<td>8659</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6841">6841</a></td>
		<td>A Framework for DNSSEC Policies and DNSSEC Practice Statements</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Problem Statement</td>
		<td>Clarification/Terminology</td>
		<td><a href="https://www.rfc-editor.org/info/rfc6840">6840</a></td>
		<td>Clarifications and Implementation Notes for DNS Security (DNSSEC)</td>
		<td></td>
	</tr>
	<tr>
		<td>Historic</td>
		<td>Service Discovery/mDNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6804">6804</a></td>
		<td>Supporting Multicast DNS Queries</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6781">6781</a></td>
		<td>DNSSEC Operational Practices, Version 2</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Service Discovery/mDNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6763">6763</a></td>
		<td>DNS-Based Service Discovery</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Service Discovery/mDNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6762">6762</a></td>
		<td>Multicast DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6761">6761</a></td>
		<td>Special-Use Domain Names </td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>Other Applications</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc6742">6742</a></td>
		<td>DNS Resource Records for the Identifier-Locator Network Protocol (ILNP)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Servicing</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6731">6731</a></td>
		<td>Improved Recursive DNS Server Selection for Multi-Interfaced Nodes</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6725">6725</a></td>
		<td>DNS Security (DNSSEC) DNSKEY Algorithm IANA Registry Updates</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>PKI Application</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc6698">6698</a></td>
		<td>The DNS-Based Authentication of Named Entities (DANE) Transport Layer Security (TLS) Protocol: TLSA</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6686">6686</a></td>
		<td>Resolution of the Sender Policy Framework (SPF) and Sender ID Experiments</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>New RRs/Codes</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6672">6672</a></td>
		<td>DNAME Redirection in the DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6652">6652</a></td>
		<td>Sender Policy Framework (SPF) Authentication Failure Reporting Using the Abuse Reporting Format</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6651">6651</a></td>
		<td>Extensions to DomainKeys Identified Mail (DKIM) for Failure Reporting</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>SRV/SVCB Functionalities</td>
		<td>Other Applications</td>
		<td><a href="https://www.rfc-editor.org/info/rfc6641">6641</a></td>
		<td>Using DNS SRV to Specify a Global File Namespace with NFS Version 4</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6605">6605</a></td>
		<td>Elliptic Curve Digital Signature Algorithm (DSA) for DNSSEC</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Clarification/Terminology</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6604">6604</a></td>
		<td>xNAME RCODE and Status Bits Clarification</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Other Applications</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6594">6594</a></td>
		<td>Use of the SHA-256 Algorithm with RSA, Digital Signature Algorithm (DSA), and Elliptic Curve DSA (ECDSA) in SSHFP Resource Records</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IPv6 Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6589">6589</a></td>
		<td>Considerations for Transitioning Content to IPv6</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Statement of Retirement</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6563">6563</a></td>
		<td>Moving A6 to Historic Status</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6541">6541</a></td>
		<td>DomainKeys Identified Mail (DKIM) Authorized Third-Party Signatures</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Filtering</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc6471">6471</a></td>
		<td>Overview of Best Email DNS-Based List (DNSBL) Operational Practices</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6452">6452</a></td>
		<td>The Unicode Code Points and Internationalized Domain Names for Applications (IDNA) - Unicode 6.0</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>PKI Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6394">6394</a></td>
		<td>Use Cases and Requirements for DNS-Based Authentication of Named Entities (DANE)</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6377">6377</a></td>
		<td>DomainKeys Identified Mail (DKIM) and Mailing Lists</td>
		<td></td>
	</tr>
	<tr>
		<td>Internet Standard</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6376">6376</a></td>
		<td>DomainKeys Identified Mail (DKIM) Signatures</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Reverse DNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6305">6305</a></td>
		<td>I'm Being Attacked by PRISONER.IANA.ORG!</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Reverse DNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6304">6304</a></td>
		<td>AS112 Nameserver Operations</td>
		<td>7534</td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Servicing</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6303">6303</a></td>
		<td>Locally Served DNS Zones</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Clarification/Terminology</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6195">6195</a></td>
		<td>Domain Name System (DNS) IANA Considerations</td>
		<td>6895</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>SRV/SVCB Functionalities</td>
		<td>Email Application</td>
		<td><a href="https://www.rfc-editor.org/info/rfc6186">6186</a></td>
		<td>Use of SRV Records for Locating Email Submission/Access Services</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Guidelines/Recommendations</td>
		<td>Servicing</td>
		<td><a href="https://www.rfc-editor.org/info/rfc6168">6168</a></td>
		<td>Requirements for Management of Name Servers for the DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IPv6 Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6147">6147</a></td>
		<td>DNS64: DNS Extensions for Network Address Translation from IPv6 Clients to IPv4 Servers</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>PKI Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6125">6125</a></td>
		<td>RFC 6125 - Representation and Verification of Domain-Based Application Service Identity within Internet Public Key Infrastructure Using X.509 (PKIX) Certificates in the Context of Transport Layer Security (TLS)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>ENUM/DDDS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6116">6116</a></td>
		<td>The E.164 to Uniform Resource Identifiers (URI) Dynamic Delegation Discovery System (DDDS) Application (ENUM)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IPv6 Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6106">6106</a></td>
		<td>IPv6 Router Advertisement Options for DNS Configuration</td>
		<td>8106</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6055">6055</a></td>
		<td>IAB Thoughts on Encodings for Internationalized Domain Names</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc6014">6014</a></td>
		<td>Cryptographic Algorithm Identifier Allocation for DNSSEC</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5992">5992</a></td>
		<td>Internationalized Domain Names Registration and Administration Guidelines for European Languages Using Cyrillic</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNS over TCP</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5966">5966</a></td>
		<td>DNS Transport over TCP - Implementation Requirements   </td>
		<td>7766</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Zone Transfer/Update</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5936">5936</a></td>
		<td>DNS Zone Transfer Protocol (AXFR)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5933">5933</a></td>
		<td>Use of GOST Signature Algorithms in DNSKEY and RRSIG Resource Records for DNSSEC</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Others</td>
		<td>Name Registration & Protocols</td>
		<td><a href="https://www.rfc-editor.org/info/rfc5910">5910</a></td>
		<td>Domain Name System (DNS) Security Extensions Mapping for the Extensible Provisioning Protocol (EPP)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5895">5895</a></td>
		<td>Mapping Characters for Internationalized Domain Names in Applications (IDNA) 2008</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5894">5894</a></td>
		<td>Internationalized Domain Names for Applications (IDNA): Background, Explanation, and Rationale</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5893">5893</a></td>
		<td>Right-to-Left Scripts for Internationalized Domain Names for Applications (IDNA)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5892">5892</a></td>
		<td>The Unicode Code Points and Internationalized Domain Names for Applications (IDNA)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5891">5891</a></td>
		<td>Internationalized Domain Names in Applications (IDNA): Protocol</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5890">5890</a></td>
		<td>Internationalized Domain Names for Applications (IDNA): Definitions and Document Framework</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>SRV/SVCB Functionalities</td>
		<td>Other Applications</td>
		<td><a href="https://www.rfc-editor.org/info/rfc5864">5864</a></td>
		<td>DNS SRV Resource Records for AFS</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5863">5863</a></td>
		<td>DomainKeys Identified Mail (DKIM) Development, Deployment, and Operations</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Reverse DNS</td>
		<td>IPv6 Application</td>
		<td><a href="https://www.rfc-editor.org/info/rfc5855">5855</a></td>
		<td>Nameservers for IPv4 and IPv6 Reverse Zones</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Filtering</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5782">5782</a></td>
		<td>DNS Blacklists and Whitelists</td>
		<td></td>
	</tr>
	<tr>
		<td>Internet Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5734">5734</a></td>
		<td>Extensible Provisioning Protocol (EPP) Transport over TCP</td>
		<td></td>
	</tr>
	<tr>
		<td>Internet Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5733">5733</a></td>
		<td>Extensible Provisioning Protocol (EPP) Contact Mapping </td>
		<td></td>
	</tr>
	<tr>
		<td>Internet Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5732">5732</a></td>
		<td>Extensible Provisioning Protocol (EPP) Host Mapping</td>
		<td></td>
	</tr>
	<tr>
		<td>Internet Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5731">5731</a></td>
		<td>Extensible Provisioning Protocol (EPP) Domain Name Mapping</td>
		<td></td>
	</tr>
	<tr>
		<td>Internet Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5730">5730</a></td>
		<td>Extensible Provisioning Protocol (EPP)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5702">5702</a></td>
		<td>Use of SHA-2 Algorithms with RSA in DNSKEY and RRSIG Resource Records for DNSSEC</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>ENUM/DDDS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5679">5679</a></td>
		<td>Locating IEEE 802.21 Mobility Services Using DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5672">5672</a></td>
		<td>RFC 4871 DomainKeys Identified Mail (DKIM) Signatures -- Update</td>
		<td>6376</td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Guidelines/Recommendations</td>
		<td>Servicing</td>
		<td><a href="https://www.rfc-editor.org/info/rfc5625">5625</a></td>
		<td>DNS Proxy Implementation Guidelines</td>
		<td></td>
	</tr>
	<tr>
		<td>Historic</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5617">5617</a></td>
		<td>DomainKeys Identified Mail (DKIM) Author Domain Signing Practices (ADSP)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5585">5585</a></td>
		<td>DomainKeys Identified Mail (DKIM) Service Overview</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IDNA/Globalization</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc5564">5564</a></td>
		<td>Linguistic Guidelines for the Use of the Arabic Language in Internet Domains</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>ENUM/DDDS</td>
		<td>Reverse DNS</td>
		<td><a href="https://www.rfc-editor.org/info/rfc5527">5527</a></td>
		<td>Combined User and Infrastructure ENUM in the e164.arpa Tree</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>ENUM/DDDS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5526">5526</a></td>
		<td>The E.164 to Uniform Resource Identifiers (URI) Dynamic Delegation Discovery System (DDDS) Application for Infrastructure ENUM</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>SRV/SVCB Functionalities</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5509">5509</a></td>
		<td>Internet Assigned Numbers Authority (IANA) Registration of Instant Messaging and Presence DNS SRV RRs for the Session Initiation Protocol (SIP)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Servicing</td>
		<td>Clarification/Terminology</td>
		<td><a href="https://www.rfc-editor.org/info/rfc5507">5507</a></td>
		<td>Design Choices When Expanding the DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Threats/Vulnerabilities & Patches</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc5452">5452</a></td>
		<td>Measures for Making DNS More Resilient against Forged Answers</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Clarification/Terminology</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5395">5395</a></td>
		<td>Domain Name System (DNS) IANA Considerations</td>
		<td>6195</td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Threats/Vulnerabilities & Patches</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5358">5358</a></td>
		<td>Preventing Use of Recursive Nameservers in Reflector Attacks</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>New RRs/Codes</td>
		<td>Other Applications</td>
		<td><a href="https://www.rfc-editor.org/info/rfc5205">5205</a></td>
		<td>Host Identity Protocol (HIP) Domain Name System (DNS) Extension</td>
		<td>8005</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IPv6 Application</td>
		<td>Reverse DNS</td>
		<td><a href="https://www.rfc-editor.org/info/rfc5158">5158</a></td>
		<td>6to4 Reverse DNS Delegation Specification</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5155">5155</a></td>
		<td>DNS Security (DNSSEC) Hashed Authenticated Denial of Existence</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5144">5144</a></td>
		<td>A Domain Availability Check (DCHK) Registry Type for the Internet Registry Information Service (IRIS)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>ENUM/DDDS</td>
		<td>Flaws/Errors & Reporting</td>
		<td><a href="https://www.rfc-editor.org/info/rfc5483">5483</a></td>
		<td>ENUM Implementation Issues and Experiences</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>ENUM/DDDS</td>
		<td>Name Registration & Protocols</td>
		<td><a href="https://www.rfc-editor.org/info/rfc5076">5076</a></td>
		<td>ENUM Validation Information Mapping for the Extensible Provisioning Protocol</td>
		<td></td>
	</tr>
	<tr>
		<td>Historic</td>
		<td>DNSSEC - Others</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5074">5074</a></td>
		<td>DNSSEC Lookaside Validation (DLV)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IPv6 Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5026">5026</a></td>
		<td>Mobile IPv6 Bootstrapping in Split Scenario</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5016">5016</a></td>
		<td>Requirements for a DomainKeys Identified Mail (DKIM) Signing Practices Protocol</td>
		<td></td>
	</tr>
	<tr>
		<td>Internet Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5011">5011</a></td>
		<td>Automated Updates of DNS Security (DNSSEC) Trust Anchors</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>IPv6 Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5006">5006</a></td>
		<td>IPv6 Router Advertisement Option for DNS Configuration</td>
		<td>6106</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Servicing</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc5001">5001</a></td>
		<td>DNS Name Server Identifier (NSID) Option</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc4986">4986</a></td>
		<td>Requirements Related to DNS Security (DNSSEC) Trust Anchor Rollover</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>DNSSEC - Others</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4956">4956</a></td>
		<td>DNS Security (DNSSEC) Opt-In</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Others</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4955">4955</a></td>
		<td>DNS Security (DNSSEC) Experiments</td>
		<td></td>
	</tr>
	<tr>
		<td>Draft Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4934">4934</a></td>
		<td>Extensible Provisioning Protocol (EPP) Transport over TCP</td>
		<td>5734</td>
	</tr>
	<tr>
		<td>Draft Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4933">4933</a></td>
		<td>Extensible Provisioning Protocol (EPP) Contact Mapping </td>
		<td>5733</td>
	</tr>
	<tr>
		<td>Draft Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4932">4932</a></td>
		<td>Extensible Provisioning Protocol (EPP) Host Mapping</td>
		<td>5732</td>
	</tr>
	<tr>
		<td>Draft Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4931">4931</a></td>
		<td>Extensible Provisioning Protocol (EPP) Domain Name Mapping</td>
		<td>5731</td>
	</tr>
	<tr>
		<td>Draft Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4930">4930</a></td>
		<td>Extensible Provisioning Protocol (EPP)</td>
		<td>5730</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Servicing</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4892">4892</a></td>
		<td>Requirements for a Mechanism Identifying a Name Server Instance</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4871">4871</a></td>
		<td>DomainKeys Identified Mail (DKIM) Signatures</td>
		<td>6376</td>
	</tr>
	<tr>
		<td>Historic</td>
		<td>Email Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4870">4870</a></td>
		<td>Domain-Based Email Authentication Using Public Keys Advertised in the DNS (DomainKeys)</td>
		<td>4871</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>ENUM/DDDS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4848">4848</a></td>
		<td>Domain-Based Application Service Location Using URIs and the Dynamic Delegation Discovery Service (DDDS)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Other Applications</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4795">4795</a></td>
		<td>Link-Local Multicast Name Resolution (LLMNR)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>ENUM/DDDS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4725">4725</a></td>
		<td>ENUM Validation Architecture</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IDNA/Globalization</td>
		<td>Name Registration & Protocols</td>
		<td><a href="https://www.rfc-editor.org/info/rfc4713">4713</a></td>
		<td>Registration and Administration Recommendations for Chinese Domain Names</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IPv6 Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4704">4704</a></td>
		<td>The Dynamic Host Configuration Protocol for IPv6 (DHCPv6) Client Fully Qualified Domain Name (FQDN) Option</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Other Applications</td>
		<td>Flaws/Errors & Reporting</td>
		<td><a href="https://www.rfc-editor.org/info/rfc4703">4703</a></td>
		<td>Resolution of Fully Qualified Domain Name (FQDN) Conflicts among Dynamic Host Configuration Protocol (DHCP) Clients</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Other Applications</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4702">4702</a></td>
		<td>The Dynamic Host Configuration Protocol (DHCP) Client Fully Qualified Domain Name (FQDN) Option</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Other Applications</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc4701">4701</a></td>
		<td>A DNS Resource Record (RR) for Encoding Dynamic Host Configuration Protocol (DHCP) Information (DHCID RR)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4698">4698</a></td>
		<td>An Address Registry (areg) Type for the Internet Registry Information Service</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Flaws/Errors & Reporting</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4697">4697</a></td>
		<td>Observed DNS Resolution Misbehavior</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IDNA/Globalization</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc4690">4690</a></td>
		<td>Review and Recommendations for Internationalized Domain Names (IDNs)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Email Application</td>
		<td>Threats/Vulnerabilities & Patches</td>
		<td><a href="https://www.rfc-editor.org/info/rfc4686">4686</a></td>
		<td>Analysis of Threats Motivating DomainKeys Identified Mail (DKIM)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4641">4641</a></td>
		<td>DNSSEC Operational Practices</td>
		<td>6781</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Transaction Authentication</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4635">4635</a></td>
		<td>HMAC SHA TSIG Algorithm Identifiers</td>
		<td>8945</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Clarification/Terminology</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4592">4592</a></td>
		<td>The Role of Wildcards in the Domain Name System</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4509">4509</a></td>
		<td>Use of SHA-256 in DNSSEC Delegation Signer (DS) Resource Records (RRs)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Data Collection & Representation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4501">4501</a></td>
		<td>Domain Name System Uniform Resource Identifiers</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IPv6 Application</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc4472">4472</a></td>
		<td>Operational Considerations and Issues with IPv6 DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4471">4471</a></td>
		<td>Derivation of DNS Name Predecessor and Successor</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4470">4470</a></td>
		<td>Minimally Covering NSEC Records and DNSSEC On-line Signing</td>
		<td></td>
	</tr>
	<tr>
		<td>Historic</td>
		<td>DNSSEC - Others</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc4431">4431</a></td>
		<td>The DNSSEC Lookaside Validation (DLV) DNS Resource Record</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>Email Application</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc4408">4408</a></td>
		<td>Sender Policy Framework (SPF) for Authorizing Use of Domains in E-Mail, Version 1</td>
		<td>7208</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>PKI Application</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc4398">4398</a></td>
		<td>Storing Certificates in the Domain Name System (DNS)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Clarification/Terminology</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4367">4367</a></td>
		<td>What's in a Name: False Assumptions about DNS Names</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Clarification/Terminology</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4343">4343</a></td>
		<td>Domain Name System (DNS) Case Insensitivity Clarification</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IPv6 Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4339">4339</a></td>
		<td>IPv6 Host Configuration of DNS Server Information Approaches</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Other Applications</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4322">4322</a></td>
		<td>Opportunistic Encryption using the Internet Key Exchange (IKE)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Others</td>
		<td>Name Registration & Protocols</td>
		<td><a href="https://www.rfc-editor.org/info/rfc4310">4310</a></td>
		<td>Domain Name System (DNS) Security Extensions Mapping for the Extensible Provisioning Protocol (EPP)</td>
		<td>5910</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4290">4290</a></td>
		<td>Suggested Practices for Registration of Internationalized Domain Names (IDN)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Other Applications</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4255">4255</a></td>
		<td>Using DNS to Securely Publish Secure Shell (SSH) Key Fingerprints</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4185">4185</a></td>
		<td>National and Local Characters for DNS Top Level Domain (TLD) Names</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Servicing</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4183">4183</a></td>
		<td>A Suggested Scheme for DNS Resolution of Networks and Gateways</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Statement of Retirement</td>
		<td>IPv6 Application</td>
		<td><a href="https://www.rfc-editor.org/info/rfc4159">4159</a></td>
		<td>Deprecation of ip6.int</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>ENUM/DDDS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4143">4143</a></td>
		<td>Facsimile Using Internet Mail (IFAX) Service of ENUM</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td>ENUM/DDDS</td>
		<td><a href="https://www.rfc-editor.org/info/rfc4114">4114</a></td>
		<td>E.164 Number Mapping for the Extensible Provisioning Protocol (EPP)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IPv6 Application</td>
		<td>Flaws/Errors & Reporting</td>
		<td><a href="https://www.rfc-editor.org/info/rfc4074">4074</a></td>
		<td>Common Misbehavior Against DNS Queries for IPv6 Addresses</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4035">4035</a></td>
		<td>Protocol Modifications for the DNS Security Extensions</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - General Operation</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc4034">4034</a></td>
		<td>Resource Records for the DNS Security Extensions</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4033">4033</a></td>
		<td>DNS Security Introduction and Requirements</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Data Collection & Representation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4027">4027</a></td>
		<td>Domain Name System Media Types</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Other Applications</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc4025">4025</a></td>
		<td>A Method for Storing IPsec Keying Material in DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3982">3982</a></td>
		<td>IRIS: A Domain Registry (dreg) Type for the Internet Registry Information Service (IRIS)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>ENUM/DDDS</td>
		<td>SRV/SVCB Functionalities</td>
		<td><a href="https://www.rfc-editor.org/info/rfc3958">3958</a></td>
		<td>Domain-Based Application Service Location Using SRV RRs and the Dynamic Delegation Discovery Service (DDDS)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3915">3915</a></td>
		<td>Domain Registry Grace Period Mapping for the Extensible Provisioning Protocol (EPP)</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>IPv6 Application</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc3901">3901</a></td>
		<td>DNS IPv6 Transport Operational Guidelines</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3845">3845</a></td>
		<td>DNS Security (DNSSEC) NextSECure (NSEC) RDATA Format</td>
		<td>4033, 4034, 4035</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNSSEC - Problem Statement</td>
		<td>Threats/Vulnerabilities & Patches</td>
		<td><a href="https://www.rfc-editor.org/info/rfc3833">3833</a></td>
		<td>Threat Analysis of the Domain Name System (DNS)</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>SRV/SVCB Functionalities</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3832">3832</a></td>
		<td>Remote Service Discovery in the Service Location Protocol (SLP) via DNS SRV</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>ENUM/DDDS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3761">3761</a></td>
		<td>The E.164 to Uniform Resource Identifiers (URI) Dynamic Delegation Discovery System (DDDS) Application (ENUM)</td>
		<td>6116, 6117</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3757">3757</a></td>
		<td>Domain Name System KEY (DNSKEY) Resource Record (RR) Secure Entry Point (SEP) Flag</td>
		<td>4033, 4034, 4035</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3755">3755</a></td>
		<td>Legacy Resolver Compatibility for Delegation Signer (DS)</td>
		<td>4033, 4034, 4035</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3743">3743</a></td>
		<td>Joint Engineering Team (JET) Guidelines for Internationalized Domain Names (IDN) Registration and Administration for Chinese, Japanese, and Korean</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3733">3733</a></td>
		<td>Extensible Provisioning Protocol (EPP) Contact Mapping</td>
		<td>4933</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3732">3732</a></td>
		<td>Extensible Provisioning Protocol (EPP) Host Mapping</td>
		<td>4932</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3731">3731</a></td>
		<td>Extensible Provisioning Protocol (EPP) Domain Name Mapping</td>
		<td>4931</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3730">3730</a></td>
		<td>Extensible Provisioning Protocol (EPP)</td>
		<td>4930</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3707">3707</a></td>
		<td>Cross Registry Internet Service Protocol (CRISP) Requirements</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3696">3696</a></td>
		<td>Application Techniques for Checking and Transformation of Names</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Reverse DNS</td>
		<td>IPv6 Application</td>
		<td><a href="https://www.rfc-editor.org/info/rfc3681">3681</a></td>
		<td>Delegation of E.F.F.3.IP6.ARPA</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Namespace</td>
		<td>Threats/Vulnerabilities & Patches</td>
		<td><a href="https://www.rfc-editor.org/info/rfc3675">3675</a></td>
		<td>.sex Considered Dangerous</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3663">3663</a></td>
		<td>Domain Administrative Data in Lightweight Directory Access Protocol (LDAP)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc3658">3658</a></td>
		<td>Delegation Signer (DS) Resource Record (RR)</td>
		<td>4033, 4034, 4035</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3655">3655</a></td>
		<td>Redefinition of DNS Authenticated Data (AD) bit</td>
		<td>4033, 4034, 4035</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IPv6 Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3646">3646</a></td>
		<td>DNS Configuration options for Dynamic Host Configuration Protocol for IPv6 (DHCPv6)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Transaction Authentication</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3645">3645</a></td>
		<td>Generic Security Service Algorithm for Secret Key Transaction Authentication for DNS (GSS-TSIG)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3632">3632</a></td>
		<td>VeriSign Registry Registrar Protocol (RRP) Version 2.0.0</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Servicing</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc3597">3597</a></td>
		<td>Handling of Unknown DNS Resource Record (RR) Types</td>
		<td></td>
	</tr>
	<tr>
		<td>Internet Standard</td>
		<td>IPv6 Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3596">3596</a></td>
		<td>DNS Extensions to Support IP Version 6</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3492">3492</a></td>
		<td>Punycode: A Bootstring encoding of Unicode for Internationalized Domain Names in Applications (IDNA)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3491">3491</a></td>
		<td>Nameprep: A Stringprep Profile for Internationalized Domain Names (IDN)</td>
		<td>5891</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3490">3490</a></td>
		<td>Internationalizing Domain Names in Applications (IDNA)</td>
		<td>5890, 5891</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Clarification/Terminology</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3467">3467</a></td>
		<td>Role of the Domain Name System (DNS)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3454">3454</a></td>
		<td>Preparation of Internationalized Strings ("stringprep")</td>
		<td>7564</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3445">3445</a></td>
		<td>Limiting the Scope of the KEY Resource Record (RR)</td>
		<td>4033, 4034, 4035</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Statement of Retirement</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3425">3425</a></td>
		<td>Obsoleting IQUERY</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>ENUM/DDDS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3405">3405</a></td>
		<td>Dynamic Delegation Discovery System (DDDS) Part Five: URI.ARPA Assignment Procedures</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>ENUM/DDDS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3404">3404</a></td>
		<td>Dynamic Delegation Discovery System (DDDS) Part Four: The Uniform Resource Identifiers (URI)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>ENUM/DDDS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3403">3403</a></td>
		<td>Dynamic Delegation Discovery System (DDDS) Part Three: The Domain Name System (DNS) Database</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>ENUM/DDDS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3402">3402</a></td>
		<td>Dynamic Delegation Discovery System (DDDS) Part Two: The Algorithm</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>ENUM/DDDS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3401">3401</a></td>
		<td>Dynamic Delegation Discovery System (DDDS) Part One: The Comprehensive DDDS</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Other Applications</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3397">3397</a></td>
		<td>Dynamic Host Configuration Protocol (DHCP) Domain Search Option</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3375">3375</a></td>
		<td>Generic Registry-Registrar Protocol Requirements</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IPv6 Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3364">3364</a></td>
		<td>Tradeoffs in Domain Name System (DNS) Support for Internet Protocol version 6 (IPv6)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IPv6 Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3363">3363</a></td>
		<td>Representing Internet Protocol version 6 (IPv6) Addresses in the Domain Name System (DNS)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Servicing</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3258">3258</a></td>
		<td>Distributing Authoritative Name Servers via Shared Unicast Addresses</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - General Operation</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc3226">3226</a></td>
		<td>DNSSEC and IPv6 A6 aware server/resolver message size requirements</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3225">3225</a></td>
		<td>Indicating Resolver Support of DNSSEC</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Statement of Retirement</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3197">3197</a></td>
		<td>Applicability Statement for DNS MIB Extensions</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Reverse DNS</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc3172">3172</a></td>
		<td>Management Guidelines & Operational Requirements for the Address and Routing Parameter Area Domain (arpa)</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>IPv6 Application</td>
		<td>Reverse DNS</td>
		<td><a href="https://www.rfc-editor.org/info/rfc3152">3152</a></td>
		<td>Delegation of IP6.ARPA</td>
		<td>3596</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNSSEC - Problem Statement</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3130">3130</a></td>
		<td>Notes from the State-Of-The-Technology: DNSSEC</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>New RRs/Codes</td>
		<td>Other Applications</td>
		<td><a href="https://www.rfc-editor.org/info/rfc3123">3123</a></td>
		<td>A DNS RR Type for Lists of Address Prefixes (APL RR)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3110">3110</a></td>
		<td>RSA/SHA-1 SIGs and RSA KEYs in the Domain Name System (DNS)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3090">3090</a></td>
		<td>DNS Security Extension Clarification on Zone Status</td>
		<td>4033, 4034, 4035</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3071">3071</a></td>
		<td>Reflections on the DNS, RFC 1591, and Categories of Domains</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>ENUM/DDDS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3026">3026</a></td>
		<td>Liaison to IETF/ISOC on ENUM</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3008">3008</a></td>
		<td>Domain Name System Security (DNSSEC) Signing Authority</td>
		<td>4033, 4034, 4035</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Zone Transfer/Update</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc3007">3007</a></td>
		<td>Secure Domain Name System (DNS) Dynamic Update</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Transaction Authentication</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2931">2931</a></td>
		<td>DNS Request and Transaction Signatures ( SIG(0)s )</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Transaction Authentication</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc2930">2930</a></td>
		<td>Secret Key Establishment for DNS (TKEY RR)</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Clarification/Terminology</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2929">2929</a></td>
		<td>Domain Name System (DNS) IANA Considerations</td>
		<td>5395</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>ENUM/DDDS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2916">2916</a></td>
		<td>E.164 Number and DNS</td>
		<td>3761</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>ENUM/DDDS</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc2915">2915</a></td>
		<td>The Naming Authority Pointer (NAPTR) DNS Resource Record</td>
		<td>3401, 3402, 3403, 3404</td>
	</tr>
	<tr>
		<td>Historic</td>
		<td>IPv6 Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2874">2874</a></td>
		<td>DNS Extensions to Support IPv6 Address Aggregation and Renumbering</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>DNS Root</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc2870">2870</a></td>
		<td>Root Name Server Operational Requirements</td>
		<td>7720</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Transaction Authentication</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc2845">2845</a></td>
		<td>Secret Key Transaction Authentication for DNS (TSIG)</td>
		<td>8945</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Name Registration & Protocols</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2832">2832</a></td>
		<td>NSI Registry Registrar Protocol (RRP) Version 1.1.0</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNS Root</td>
		<td>Clarification/Terminology</td>
		<td><a href="https://www.rfc-editor.org/info/rfc2826">2826</a></td>
		<td>IAB Technical Comment on the Unique DNS Root</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>IDNA/Globalization</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2825">2825</a></td>
		<td>A Tangled Web: Issues of I18N, Domain Names, and the Other Internet protocols</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>SRV/SVCB Functionalities</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc2782">2782</a></td>
		<td>A DNS RR for specifying the location of services (DNS SRV)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>New RRs/Codes</td>
		<td>Other Applications</td>
		<td><a href="https://www.rfc-editor.org/info/rfc2694">2694</a></td>
		<td>DNS extensions to Network Address Translators (DNS_ALG)</td>
		<td></td>
	</tr>
	<tr>
		<td>Historic</td>
		<td>Data Collection & Representation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2673">2673</a></td>
		<td>Binary Labels in the Domain Name System</td>
		<td>6891</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>New RRs/Codes</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2672">2672</a></td>
		<td>Non-Terminal DNS Name Redirection</td>
		<td>6672</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>EDNS & Extensions</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2671">2671</a></td>
		<td>Extension Mechanisms for DNS (EDNS0)</td>
		<td>6891</td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2606">2606</a></td>
		<td>Reserved Top Level DNS Names</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2541">2541</a></td>
		<td>DNS Security Operational Considerations</td>
		<td>4641</td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2540">2540</a></td>
		<td>Detached Domain Name System (DNS) Information</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Transaction Authentication</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2539">2539</a></td>
		<td>Storage of Diffie-Hellman Keys in the Domain Name System (DNS)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>PKI Application</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc2538">2538</a></td>
		<td>Storing Certificates in the Domain Name System (DNS)</td>
		<td>4398</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - Algorithms/Keys</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2537">2537</a></td>
		<td>RSA/MD5 KEYs and SIGs in the Domain Name System (DNS)</td>
		<td>3110</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Transaction Authentication</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2536">2536</a></td>
		<td>DSA KEYs and SIGs in the Domain Name System (DNS)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2535">2535</a></td>
		<td>Domain Name System Security Extensions</td>
		<td>4033, 4034, 4035</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2517">2517</a></td>
		<td>Building Directories from DNS: Experiences from WWWSeeker</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2352">2352</a></td>
		<td>A Convention For Using Legal Names as Domain Names</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2345">2345</a></td>
		<td>Domain Names and Company Name Retrieval</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Reverse DNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2317">2317</a></td>
		<td>Classless IN-ADDR.ARPA delegation</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Servicing</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2308">2308</a></td>
		<td>Negative Caching of DNS Queries (DNS NCACHE)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2240">2240</a></td>
		<td>A Legal Basis for Domain Name Allocation</td>
		<td>2352</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Transaction Authentication</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc2230">2230</a></td>
		<td>Key Exchange Delegation Record for the DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Other Applications</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2219">2219</a></td>
		<td>Use of DNS Aliases for Network Services</td>
		<td></td>
	</tr>
	<tr>
		<td>Best Current Practice</td>
		<td>Servicing</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2182">2182</a></td>
		<td>Selection and Operation of Secondary DNS Servers</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Clarification/Terminology</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2181">2181</a></td>
		<td>Clarifications to the DNS Specification</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>ENUM/DDDS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2168">2168</a></td>
		<td>Resolution of Uniform Resource Identifiers using the Domain Name System</td>
		<td>3401, 3402, 3403, 3404</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>New RRs/Codes</td>
		<td>Other Applications</td>
		<td><a href="https://www.rfc-editor.org/info/rfc2163">2163</a></td>
		<td>Using the Internet DNS to Distribute MIXER Conformant Global Address Mapping (MCGAM)</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2146">2146</a></td>
		<td>U.S. Government Internet Domain Names</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Zone Transfer/Update</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2137">2137</a></td>
		<td>Secure Domain Name System Dynamic Update</td>
		<td>3007</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Zone Transfer/Update</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2136">2136</a></td>
		<td>Dynamic Updates in the Domain Name System (DNS UPDATE)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>DNSSEC - General Operation</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2065">2065</a></td>
		<td>Domain Name System Security Extensions</td>
		<td>2535</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc2053">2053</a></td>
		<td>The AM (Armenia) Domain</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>SRV/SVCB Functionalities</td>
		<td>New RRs/Codes</td>
		<td><a href="https://www.rfc-editor.org/info/rfc2052">2052</a></td>
		<td>A DNS RR for specifying the location of services (DNS SRV)</td>
		<td>2782</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>DNS Root</td>
		<td>Guidelines/Recommendations</td>
		<td><a href="https://www.rfc-editor.org/info/rfc2010">2010</a></td>
		<td>Operational Criteria for Root Name Servers</td>
		<td>2870</td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Zone Transfer/Update</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1996">1996</a></td>
		<td>A Mechanism for Prompt Notification of Zone Changes (DNS NOTIFY)</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Zone Transfer/Update</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1995">1995</a></td>
		<td>Incremental Zone Transfer in DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>Servicing</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1982">1982</a></td>
		<td>Serial Number Arithmetic</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1956">1956</a></td>
		<td>Registration in the MIL Domain</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Flaws/Errors & Reporting</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1912">1912</a></td>
		<td>Common DNS Operational and Configuration Errors</td>
		<td></td>
	</tr>
	<tr>
		<td>Proposed Standard</td>
		<td>IPv6 Application</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1886">1886</a></td>
		<td>DNS Extensions to support IP version 6</td>
		<td>3596</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Other Applications</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1877">1877</a></td>
		<td>PPP Internet Protocol Control Protocol Extensions for Name Server Addresses</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>New RRs/Codes</td>
		<td>Other Applications</td>
		<td><a href="https://www.rfc-editor.org/info/rfc1876">1876</a></td>
		<td>A Means for Expressing Location Information in the Domain Name System</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1816">1816</a></td>
		<td>U.S. Government Internet Domain Names</td>
		<td>2146</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1811">1811</a></td>
		<td>U.S. Government Internet Domain Names</td>
		<td>1816</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Servicing</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1794">1794</a></td>
		<td>DNS Support for Load Balancing</td>
		<td></td>
	</tr>
	<tr>
		<td>Historic</td>
		<td>New RRs/Codes</td>
		<td>Other Applications</td>
		<td><a href="https://www.rfc-editor.org/info/rfc1788">1788</a></td>
		<td>ICMP Domain Name Messages</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Servicing</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1713">1713</a></td>
		<td>Tools for DNS debugging</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>New RRs/Codes</td>
		<td>Other Applications</td>
		<td><a href="https://www.rfc-editor.org/info/rfc1712">1712</a></td>
		<td>DNS Encoding of Geographical Location</td>
		<td></td>
	</tr>
	<tr>
		<td>Historic</td>
		<td>New RRs/Codes</td>
		<td>Other Applications</td>
		<td><a href="https://www.rfc-editor.org/info/rfc1706">1706</a></td>
		<td>DNS NSAP Resource Records</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>New RRs/Codes</td>
		<td>Other Applications</td>
		<td><a href="https://www.rfc-editor.org/info/rfc1664">1664</a></td>
		<td>Using the Internet DNS to Distribute RFC1327 Mail Address Mapping Tables</td>
		<td>2163</td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>New RRs/Codes</td>
		<td>Other Applications</td>
		<td><a href="https://www.rfc-editor.org/info/rfc1637">1637</a></td>
		<td>DNS NSAP Resource Records</td>
		<td>1706</td>
	</tr>
	<tr>
		<td>Historic</td>
		<td>New RRs/Codes</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1612">1612</a></td>
		<td>DNS Resolver MIB Extensions</td>
		<td></td>
	</tr>
	<tr>
		<td>Historic</td>
		<td>New RRs/Codes</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1611">1611</a></td>
		<td>DNS Server MIB Extensions</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1591">1591</a></td>
		<td>Domain Name System Structure and Delegation</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Flaws/Errors & Reporting</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1537">1537</a></td>
		<td>Common DNS Data File Configuration Errors</td>
		<td>1912</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Flaws/Errors & Reporting</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1536">1536</a></td>
		<td>Common DNS Implementation Errors and Suggested Fixes</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Threats/Vulnerabilities & Patches</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1535">1535</a></td>
		<td>A Security Problem and Proposed Correction With Widely Deployed DNS Software</td>
		<td></td>
	</tr>
	<tr>
		<td>Historic</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1528">1528</a></td>
		<td>Principles of Operation for the TPC.INT Subdomain: Remote Printing -- Technical Procedures</td>
		<td>9121</td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1480">1480</a></td>
		<td>The US Domain</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>New RRs/Codes</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1464">1464</a></td>
		<td>Using the Domain Name System To Store Arbitrary String Attributes</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Clarification/Terminology</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1401">1401</a></td>
		<td>Correspondence between the IAB and DISA on the use of DNS</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Other Applications</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1394">1394</a></td>
		<td>Relationship of Telex Answerback Codes to Internet Domains</td>
		<td></td>
	</tr>
	<tr>
		<td>Informational</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1386">1386</a></td>
		<td>The US Domain</td>
		<td>1480</td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>Other Applications</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1383">1383</a></td>
		<td>An Experiment in DNS Based IP Routing</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>New RRs/Codes</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1348">1348</a></td>
		<td>DNS NSAP RRs</td>
		<td>1637</td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>Namespace</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1279">1279</a></td>
		<td>X.500 and Domains</td>
		<td></td>
	</tr>
	<tr>
		<td>Experimental</td>
		<td>New RRs/Codes</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1183">1183</a></td>
		<td>New DNS RR Definitions</td>
		<td></td>
	</tr>
	<tr>
		<td>Internet Standard</td>
		<td>Clarification/Terminology</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1123">1123</a></td>
		<td>Requirements for Internet Hosts -- Application and Support</td>
		<td></td>
	</tr>
	<tr>
		<td>Unknown</td>
		<td>Reverse DNS</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1101">1101</a></td>
		<td>DNS encoding of network names and other types</td>
		<td></td>
	</tr>
	<tr>
		<td>Internet Standard</td>
		<td>Core DNS documents</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1035">1035</a></td>
		<td>Domain names - implementation and specification</td>
		<td></td>
	</tr>
	<tr>
		<td>Internet Standard</td>
		<td>Core DNS documents</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1034">1034</a></td>
		<td>Domain names - concepts and facilities</td>
		<td></td>
	</tr>
	<tr>
		<td>Unknown</td>
		<td>Core DNS documents</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc1033">1033</a></td>
		<td>Domain Administrators Operations Guide</td>
		<td></td>
	</tr>
	<tr>
		<td>Unknown</td>
		<td>Core DNS documents</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc973">973</a></td>
		<td>Domain System Changes and Observations</td>
		<td>1034, 1035</td>
	</tr>
	<tr>
		<td>Unknown</td>
		<td>Core DNS documents</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc883">883</a></td>
		<td>DOMAIN NAMES - IMPLEMENTATION and SPECIFICATION</td>
		<td>1034, 1035</td>
	</tr>
	<tr>
		<td>Unknown</td>
		<td>Core DNS documents</td>
		<td></td>
		<td><a href="https://www.rfc-editor.org/info/rfc882">882</a></td>
		<td>DOMAIN NAMES - CONCEPTS and FACILITIES</td>
		<td>1034, 1035</td>
	</tr>
</table>
	<script>
		//勾选的tags
		var chacked_status = {};
		var chacked_topic = {};
		// 获取表格中的所有不重复的status，并生成对应的 checkbox
		var names = [];
		var table = document.getElementById("myTable");
		var rows = table.getElementsByTagName("tr");
		for (var i = 1; i < rows.length; i++) {
			var name = rows[i].getElementsByTagName("td")[0].innerText;
			if (names.indexOf(name) === -1) {
				names.push(name);
			}
			chacked_status[name] = 1
		}
		names.sort();
		var checkboxesDiv = document.getElementById("checkboxes");
		var tr = document.createElement("tr");
		tr.style.borderTop = '1px solid #dee2e6';
		var tdc = 0;
		for (var i = 0; i < names.length; i++) {
			var td = document.createElement("td");
			td.style.borderTop = 'none';
			td.style.borderBottom = 'none';
			var checkbox = document.createElement("input");
			name = names[i];
			checkbox.type = "checkbox";
			checkbox.name = "names";
			checkbox.value = name;
			td.appendChild(checkbox);
			td.appendChild(document.createTextNode(" " + name));
			tr.appendChild(td);
			tdc++;
			if (tdc === 8) {
				checkboxesDiv.appendChild(tr);
				tr = document.createElement('tr')
				tdc = 0;
			}
		}
		if (tdc != 0) {
			while (tdc < 8) {
				td = document.createElement("td");
				td.style.borderTop = 'none';
				td.style.borderBottom = 'none';
				td.textContent = "";
				tr.appendChild(td);
				tdc++;
			};
			checkboxesDiv.appendChild(tr);
		};
		// 获取所有点选框  
		var checkboxes = document.getElementsByName('names');
		// 遍历所有点选框并将它们的状态设置为已勾选  
		for (var i = 0; i < checkboxes.length; i++) {
			checkboxes[i].checked = true;
		}
		// 绑定事件，点击 checkbox 更新表格
		var checkboxes = document.getElementsByName("names");
		for (var i = 0; i < checkboxes.length; i++) {
			checkboxes[i].addEventListener("change", function () {
				if (this.checked) {
					//console.log("add"+this.value);
					chacked_status[this.value] = 1;
				} else {
					delete (chacked_status[this.value]);
					//console.log("delete"+this.value);
				}
				upgradetable();
			});
		}
		////////////////////////////////////////////////////////////////////////////
		var specification = { "Clarification/Terminology": 1, "Core DNS documents": 1, "DNS over TCP": 1, "EDNS & Extensions": 1, "IDNA/Globalization": 1, "Name Registration & Protocols": 1, "Namespace": 1, "New RRs/Codes": 1, "Reverse DNS": 1, "Statement of Retirement": 1, "Zone Transfer/Update": 1 };
		///
		var operation = { "Data Collection & Representation": 1, "DNS Root": 1, "Flaws/Errors & Reporting": 1, "Guidelines/Recommendations": 1, "Servicing": 1 };
		///
		var security = { "DNS Privacy": 1, "DNSSEC - Algorithms/Keys": 1, "DNSSEC - General Operation": 1, "DNSSEC - Others": 1, "DNSSEC - Problem Statement": 1, "Encrypted DNS": 1, "Filtering": 1, "Threats/Vulnerabilities & Patches": 1, "Transaction Authentication": 1 };
		///
		var use = { "Email Application": 1, "IPv6 Application": 1, "Other Applications": 1, "PKI Application": 1, "Service Discovery/mDNS": 1, "SRV/SVCB Functionalities": 1, "ENUM/DDDS": 1, "Other use": 1 };
		// 获取表格中的所有不重复的topics，并生成对应的 checkbox
		var topics = [];
		var table = document.getElementById("myTable");
		var rows = table.getElementsByTagName("tr");
		for (var i = 1; i < rows.length; i++) {
			var name1 = rows[i].getElementsByTagName("td")[1].innerText;
			var name2 = rows[i].getElementsByTagName("td")[2].innerText;
			if (topics.indexOf(name1) === -1 && name1 != "") {
				topics.push(name1);
			}
			if (topics.indexOf(name2) === -1 && name2 != "") {
				topics.push(name2);
			}
		}
		chacked_topic["Core DNS documents"] = 1
		topics.sort();
		//添加topic按钮
		var checkboxesDiv = document.getElementById("checkboxes_topics");
		//首先添加 specification
		var tdc = 0;
		var tr = document.createElement("tr");
		tr.style.borderTop = '1px solid #dee2e6';
		var td = document.createElement("td");
		td.textContent = "Specification";
		td.style.borderTop = 'none';
		td.style.borderBottom = 'none';
		td.style.fontWeight = 'bold';
		tr.appendChild(td);
		// console.log("total tags:" + topics.length);
		for (var i = 0; i < topics.length; i++) {
			name = topics[i];
			if (!(name in specification)) {
				continue;
			};
			// console.log(name);
			var td = document.createElement("td");
			td.style.borderTop = 'none';
			td.style.borderBottom = 'none';
			var checkbox = document.createElement("input");
			checkbox.type = "checkbox";
			checkbox.name = "tag23";
			checkbox.value = name;
			td.appendChild(checkbox);
			td.appendChild(document.createTextNode(" " + name));
			tr.appendChild(td);
			tdc++;
			if (tdc === 5) {
				checkboxesDiv.appendChild(tr);
				tr = document.createElement('tr')
				td = document.createElement("td");
				td.style.borderTop = 'none';
				td.style.borderBottom = 'none'; td.textContent = "";
				tr.appendChild(td)
				tdc = 0;
			}
		}
		if (tdc != 0) {
			while (tdc < 5) {
				td = document.createElement("td");
				td.style.borderTop = 'none';
				td.style.borderBottom = 'none';
				td.textContent = "";
				tr.appendChild(td);
				tdc++;
			};
			checkboxesDiv.appendChild(tr);
		};
		//然后operation
		var tdc = 0;
		var tr = document.createElement("tr");
		tr.style.borderTop = '1px solid #dee2e6';
		var td = document.createElement("td");
		td.style.borderTop = 'none';
		td.style.borderBottom = 'none';
		td.textContent = "Operation";
		td.style.fontWeight = 'bold';
		tr.appendChild(td);
		// console.log("total tags:" + topics.length);
		for (var i = 0; i < topics.length; i++) {
			var td = document.createElement("td");
			td.style.borderTop = 'none';
			td.style.borderBottom = 'none';
			var checkbox = document.createElement("input");
			name = topics[i];
			if (!(name in operation)) {
				continue;
			};
			checkbox.type = "checkbox";
			checkbox.name = "tag23";
			checkbox.value = name;
			td.appendChild(checkbox);
			td.appendChild(document.createTextNode(" " + name));
			tr.appendChild(td);
			tdc++;
			if (tdc === 5) {
				checkboxesDiv.appendChild(tr);
				tr = document.createElement('tr')
				td = document.createElement("td");
				td.style.borderTop = 'none';
				td.style.borderBottom = 'none';
				td.textContent = "";
				tr.appendChild(td)
				tdc = 0;
			}
		}
		if (tdc != 0) {
			while (tdc < 5) {
				td = document.createElement("td");
				td.style.borderTop = 'none';
				td.style.borderBottom = 'none'; td.textContent = "";
				tr.appendChild(td);
				tdc++;
			};
			checkboxesDiv.appendChild(tr);
		};
		//Security
		var tdc = 0;
		var tr = document.createElement("tr");
		tr.style.borderTop = '1px solid #dee2e6';
		var td = document.createElement("td");
		td.style.borderTop = 'none';
		td.style.borderBottom = 'none';
		td.textContent = "Security";
		td.style.fontWeight = 'bold';
		tr.appendChild(td);
		// console.log("total tags:" + topics.length);
		for (var i = 0; i < topics.length; i++) {
			var td = document.createElement("td");
			td.style.borderTop = 'none';
			td.style.borderBottom = 'none';
			var checkbox = document.createElement("input");
			name = topics[i];
			if (!(name in security)) {
				continue;
			};
			checkbox.type = "checkbox";
			checkbox.name = "tag23";
			checkbox.value = name;
			td.appendChild(checkbox);
			td.appendChild(document.createTextNode(" " + name));
			tr.appendChild(td);
			tdc++;
			if (tdc === 5) {
				checkboxesDiv.appendChild(tr);
				tr = document.createElement('tr')
				td = document.createElement("td");
				td.style.borderTop = 'none';
				td.style.borderBottom = 'none';
				td.textContent = "";
				tr.appendChild(td)
				tdc = 0;
			}
		}
		if (tdc != 0) {
			while (tdc < 5) {
				td = document.createElement("td");
				td.style.borderTop = 'none';
				td.style.borderBottom = 'none';
				td.textContent = "";
				tr.appendChild(td);
				tdc++;
			};
			checkboxesDiv.appendChild(tr);
		};
		//use
		var tdc = 0;
		var tr = document.createElement("tr");
		tr.style.borderTop = '1px solid #dee2e6';
		var td = document.createElement("td");
		td.style.borderTop = 'none';
		td.style.borderBottom = 'none';
		td.textContent = "Application";
		td.style.fontWeight = 'bold';
		tr.appendChild(td);
		// console.log("total tags:" + topics.length);
		for (var i = 0; i < topics.length; i++) {
			var td = document.createElement("td");
			td.style.borderTop = 'none';
			td.style.borderBottom = 'none';
			var checkbox = document.createElement("input");
			name = topics[i];
			if (!(name in use)) {
				continue;
			};
			checkbox.type = "checkbox";
			checkbox.name = "tag23";
			checkbox.value = name;
			td.appendChild(checkbox);
			td.appendChild(document.createTextNode(" " + name));
			tr.appendChild(td);
			tdc++;
			if (tdc === 5) {
				checkboxesDiv.appendChild(tr);
				tr = document.createElement('tr')
				td = document.createElement("td");
				td.style.borderTop = 'none';
				td.style.borderBottom = 'none';
				td.textContent = "";
				tr.appendChild(td)
				tdc = 0;
			}
		}
		if (tdc != 0) {
			while (tdc < 5) {
				td = document.createElement("td");
				td.style.borderTop = 'none';
				td.style.borderBottom = 'none';
				td.textContent = "";
				tr.appendChild(td);
				tdc++;
			};
			checkboxesDiv.appendChild(tr);
		};
		// 获取所有点选框  
		var checkboxes = document.getElementsByName('tag23');
		// 遍历所有点选框并将它们的状态设置为已勾选  
		for (var i = 0; i < checkboxes.length; i++) {
			if (checkboxes[i].value === "Core DNS documents") {
				checkboxes[i].checked = true;
			};
		}
		upgradetable();
		// 绑定事件，点击 checkbox 筛选表格
		var checkboxes = document.getElementsByName("tag23");
		for (var i = 0; i < checkboxes.length; i++) {
			checkboxes[i].addEventListener("change", function () {
				if (this.checked) {
					chacked_topic[this.value] = 1;
				} else {
					delete (chacked_topic[this.value]);
				}
				upgradetable();
			});
		}
		////////////////////////////////////////////////////////////////
		// 全选status
		var button_rfc_status_s = document.getElementById('rfc_status_s');
		// 添加点击事件监听器
		button_rfc_status_s.addEventListener('click', function () {
			var checkboxes = document.getElementsByName('names');
			for (var i = 0; i < checkboxes.length; i++) {
				checkboxes[i].checked = true;
				chacked_status[checkboxes[i].value] = 1
			}
			upgradetable();
		});
		// 全不选status
		var button_rfc_status_uns = document.getElementById('rfc_status_uns');
		// 添加点击事件监听器
		button_rfc_status_uns.addEventListener('click', function () {
			var checkboxes = document.getElementsByName('names');
			for (var i = 0; i < checkboxes.length; i++) {
				checkboxes[i].checked = false;
				delete chacked_status[checkboxes[i].value];
			}
			upgradetable();
		});
		// 全选topic
		var button_topic_s = document.getElementById('topic_s');
		// 添加点击事件监听器
		button_topic_s.addEventListener('click', function () {
			var checkboxes = document.getElementsByName('tag23');
			for (var i = 0; i < checkboxes.length; i++) {
				checkboxes[i].checked = true;
				chacked_topic[checkboxes[i].value] = 1;
			}
			upgradetable()
		});
		// 全不选topic
		var button_topic_uns = document.getElementById('topic_uns');
		// 添加点击事件监听器
		button_topic_uns.addEventListener('click', function () {
			var checkboxes = document.getElementsByName('tag23');
			for (var i = 0; i < checkboxes.length; i++) {
				checkboxes[i].checked = false;
				delete chacked_topic[checkboxes[i].value]
			}
			upgradetable()
		});
		function upgradetable() {
			var shown_count = 0;
			//console.log(chacked_status)
			//console.log(chacked_topic)
			var table = document.getElementById("myTable");
			var rows = table.getElementsByTagName("tr");
			for (var j = 1; j < rows.length; j++) {
				var tag0 = rows[j].getElementsByTagName("td")[0].innerText;
				var tag1 = rows[j].getElementsByTagName("td")[1].innerText;
				var tag2 = rows[j].getElementsByTagName("td")[2].innerText;
				//console.log(tag0)
				if ((tag0 in chacked_status) && ((tag1 in chacked_topic) || (tag2 in chacked_topic))) {
					rows[j].style.display = "";
					shown_count++;
				} else {
					rows[j].style.display = "none";
				}
			}
			// 获取正在现实的RFC数量元素
			var numberSpan = document.getElementById('rfcshowed');
			// 更新数字
			numberSpan.textContent = shown_count;
		}
		// 获取元素
		var numberSpan = document.getElementById('rfcsnumber');
		// 更新数字
		var newNumber = rows.length - 1;
		numberSpan.textContent = newNumber;
		// 获取元素
		var numberSpan = document.getElementById('labelsnumber');
		// 更新数字
		var newNumber = topics.length;
		numberSpan.textContent = newNumber;
	</script>
</body>