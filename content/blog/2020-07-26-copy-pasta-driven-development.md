<!-- title:Copy/Pasta Driven Development® -->


As seen in numerous pull requests, the conversation goes something like this:

> Me: “Interesting solution. Where did this come from?”
> 
> Colleague: “I found it on Stack Overflow.”
> 
> Me: “Did you copy/paste it?”
> 
> Colleague: “Yes”
> 
> Me: “Do you **KNOW** what it does?”
> 
> Colleague: “Um… yeah.”
> 
> Me: “What does it do then? What are the implications of this solution?”
> 
> Colleague: “Let me find out…”

This is what I call, the Copy/Pasta Driven Development® pattern. 

Don’t know what to do? Google it. Find it. Copy it. Paste it. Profit?

Probably not. 

Everytime you select code from a browser, followed by pressing cmd+C and then cmd+V, I surmise you are robbing yourself of precious time to up your knowledge.

Copy/pasting is even more harmful, I argue, to more junior developers. Junior developers need to be able to bang their heads against a problem a bit before realizing their pitfalls, eventually coming out of the deep end with a clearer vision of the tools they use. By copy/pasting, you short circuit this learning opportunity, and end up looking for the “easy answers” without understanding **why** that is the easy answer. 

Before I continue, I must say that copy/paste is a very powerful concept, something that we all do. Almost magical. However, just like everything in life, too much of something can be detrimental. 

By copy/pasting, you are taking someone else’s answer to a very specific problem and using it for yours. On the face of it, that statement seems perfectly reasonable, right? But the trouble comes when you do not understand, or even worse, do not contemplate its interaction with your specific problem.

To build up the habit, referencing someone else’s answer to solve your given problem is perfectly valid. If you are to use the given solution, do not copy/paste it. Instead, line by line, type it out. While typing, go line by line figuring out what every variable, argument, loop, etc. is doing. Don’t know what that argument does? Look it up. Don’t get this loop? Write it out so you do understand it. The key here is not being able to understand the code you are writing, but being able to read code quickly. This practice will help with that.

Finally, yes, there are times to copy/paste. For instance, if you are doing something repeatedly and you understand its functionality, you probably can copy/paste. Even better, you should figure out how to automate that repetitive task. However, you should not be copy/pasting stuff that you don’t understand. 

Take the couple of minutes to fully digest what is happening in the code you are executing. You will not regret it. 

Bonus conversation:

> Colleague: “Hey, Andrew, this piece of code doesn’t work like it’s supposed to. Could you take a look? My tests are failing, and I don't know why.”
> 
> Me: “Where did this new line come from?”
> 
> Colleague: “From this other file.”
> 
> Me: “So, you copied it?”
> 
> Colleague: “Yeah”
> 
> Me: “Do you know what it’s doing then?”
> 
> Colleague: “Not really...”
> 
> Me: “Ok, then delete that code and start over without copy/pasting.”
10 minutes later I hear...
> 
> Colleague: "Ohhhhhhhh!"
