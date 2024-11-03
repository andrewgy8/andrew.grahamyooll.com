<!-- title:Flask and Javascript Testing -->

<p>There comes a time in a Flask applications lifecycle where javascript testing may become necessary. You might have lots of jQuery laying around. Or get that sneaking feeling like you are going to start adding some Vue.js code into your project.</p>

<p>For whatever reason, you’ll be happy to know that it’s not a huge undertaking and can be quite simple and highly effective.</p>

<p>For this example I have used the <a href="https://github.com/pallets/flask/tree/master/examples/flaskr">Flaskr</a> example from the official Flask repository.</p>  

<p>Once you have your project, lets get started!</p>

<p>While you are in the root directory, you will want to run:
 {% highlight bash %}npm init{% endhighlight %} You can fill all the prompts out now or later.  Its up to you. </p>

<p>This will result in a {% highlight bash %}package.json{% endhighlight %} file.</p>

<p>Then run: </p>
{% highlight bash %}
npm install karma karma-chrome-launcher karma-jasmine jasmine-core karma-browserify watchify requirejs --save-dev{% endhighlight %}

<p>This will install all the necessary npm packages to run Karma in our Flask application.  </p>

<p>We then run: </p>
{% highlight bash %}
karma init{% endhighlight %}

<p>This will prompt you with a bunch of questions. You can answer them as you like. </p>

<p>For this post, there are two questions that concern me:</p>
<ol> 
	<li>{% highlight bash %}Do you want to use Require.js ? > yes{% endhighlight %}</li>

	<li>{% highlight bash %}What is the location of your source and test files ? > test/**/*.spec.js{% endhighlight %}</li>
</ol>

<p>That just means that we are going to look and put all our javascript tests into a test/something directory. And importantly, the test names all end with spec.js.  For example, something.spec.js</p>

<p>We can then test it out by creating a test in the something.spec.js file:</p>

{% highlight javascript %}
describe("A suite", function() {
  it("contains spec with an expectation", function() {
    expect(true).toBe(true);
  });
});{% endhighlight %}

<p>And then we save and run:</p> 
{% highlight bash %}karma start{% endhighlight %}
<p>Voila! Our tests should pass with green.</p>

<p>Another cool thing about this set up is that the code will be watched.  So when you change any files, the tests will rerun to make sure everything is still passing.  </p>

<p>I recommend you read through the <a href="https://jasmine.github.io/2.0/introduction.html">Jasmine</a> and <a href="https://karma-runner.github.io/2.0/index.html">Karma</a> docs. You can do a lot of cool stuff in the karma.config.js file.</p>

<p>I’ll post some more on that later!</p>
