# SageChat

Introducing the productivity solution in the age of the Silver Tsunami.

Submission for [Aifinity 2023](https://aifinity-2023.devpost.com/).

## The current problem

With the population of the elderly only poised to skyrocket and the number of working adults to diminish, the workload on social workers and governmental organizations to look after the aged population is
getting heavier by the day.

Social workers would have to visit more elderlies throughout the day and governmental organization's manpower would be spreadout thin to cover the whole population.

## The solution

We propose this AI innovation to alleviate the stress and take on the workload for these sectors.

SageChat will be like a friendly neighbour to the elderlies, checking in everyday and being there for them when they want to talk about the old times.

However, it isn't just a chat bot. 

While conversing with the elderlies, it will be able to detect the sentiments of elderlies, how they are feeling, whether they had a good nights sleep, whether they took the right medications and so much more. 

Of course! Privacy of the conversation is number one priority, thus the bot will only collect crucial medical related information. No other parts of the conversations would be stored in the database.

With these information, the bot would help streamline the work for the social workers. Instead of stressing themselves out to go visit and check up on every elderly, they can focus their limited attention and time onto those elderlies that are in dire need of human or medical assistance. 

The bot would periodically report back with medical information of the elderlies it converses with. With this collated information, the social workers and organizations will have an easier and more productive time identifying those elderlies in need of care and attention.

This can also be relayed to the respective doctors whom can prescribe more medication or even suggest a visit to the hospital.

## Future Improvements

With more data collected, I believe our AI will be able to more accurately detect crucial medical information from conversations using NLP technologies. 

Hopefully, it will be able to detect whether the elderly is showing early signs of dementia or other illnesses that may go unnoticed for a long time. 

This would be both beneficial to the social industry and to the elderlies. 

With this, the AI will also be able to better protect conversation privacy, preventing any unnecessary leaks of information and privacy.

## Files

In the root folder, you can type in `npm start`
which will run the chat bot interface that will be shown to the elderlies. 

In this webpage, the elderlies will be able to speak into it and a voice will talk back to them.

Behind the scenes, with the conversation data collected, we used AWS Comprehend to detect sentiment throughout the conversation and relay extremely negative conversations back to the workers. 

Additionally, we also used Med7, a python-based AI library that is effective in detecting medication related data throughout the conversation.

## Tech used 

* text-davinci-003 - OpenAi
* AWS Comprehend - Amazon
* Med7 - HuggingFace
* React JS