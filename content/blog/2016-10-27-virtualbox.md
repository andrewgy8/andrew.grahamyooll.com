--- 
title: VirtualBox on Kali-Linux 
---

<h2 class="section-heading">Want to run a virtual machine within Kali Linux?</h2>

<p>You can use VirtualBox easily on your setup.</p>

<h2 class="section-heading">Here is how to do it</h2>

<ol>
	<li>Execute {% highlight bash %}apt-get update{% endhighlight %} What does it do? Looks into /etc/apt/sources.list, and ‘re-synchronize the package index files from their sources’.</li>
	<li>Execute {% highlight bash %}apt-get upgrade{% endhighlight %} What does it do? Looks into /etc/apt/sources.list and grabs new versions of those listed packages.</li>
	<li>Execute {% highlight bash %}apt-get dist-upgrade{% endhighlight %} What does it do? A more intelligent {% highlight bash %}apt-get upgrade{% endhighlight %} that will upgrade and remove package dependencies.<sup>1</sup></li>
	<li>Execute {% highlight bash %}apt-get install linux-headers-$(uname -r){% endhighlight %}</li>
	<li>Go to the VirtualBox downloads page. Checkout the various versions.  Every released version of VirtualBox will have various distribution packages for numerous OS’. <br>As of writing this, I am using Kali Linux v. 2016-2. Therefore, I downloaded VirtualBox v. 5.1.12 and am able to run the wheezy codename on my machine. And you'll most likely want to install .amd64.<sup>2</sup> If you are unsure, you will receive an error when going onto the next step. Execute {% highlight bash %}wget download.virtualbox.org/virtualbox/5.1.1/virtualbox-5.1_5.1.12-112440~Debian~wheezy_amd64.deb{% endhighlight %} 
	</li>
	<li>`cd` into the directory for the download that you just performed.  If you `ls`, it will most likely be in the current working directory. Run  {% highlight bash %}dpkg -i virtualbox-5.1_5.1.12-112440~Debian~wheezy_amd64.deb` to install the package{% endhighlight %}</li>
	<li>Important, execute {% highlight bash %}reboot{% endhighlight %} And that should be it! </li>
</ol>

<h2 class="section-heading">References</h2>
<ul>
	<li>
		<sup>1</sup><a href="http://askubuntu.com/questions/222348/what-does-sudo-apt-get-update-do">http://askubuntu.com/questions/222348/what-does-sudo-apt-get-update-do</a>
	</li>
	<li>
		<sup>2</sup><a href="http://askubuntu.com/a/54298">http://askubuntu.com/a/54298</a>
	</li>
</ul>
