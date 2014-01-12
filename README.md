chin up
=======

### Why? ###
To become the best I can be, I need motivation, I need to get my chin up.

### How do you measure? ###
Every metric that I believe significantly effects my motivation and health will be measured on a scale frome 1 to 10.
If there is something significant to note, I'll put that down as well. However, the main goal is to motivate myself through
numbers and statistics.

**1 being** the worst, least effort I could possibly put in and **10 being** the best, most effort I could possibly put in.

### When will you be... done? ###
I don't ever expect to be a 10 in all areas all the time, so there will always be room for improvement! I need/want some
motivation in my life these days. It's strange being 25 and having your whole life ahead of you. So crippling to want to
pursue Jiu Jitsu, Fishing, Programming, Gaming, Olympic Lifting, Powerlifting, Traveling, starting a family, etc. etc.

It's difficult to make a decision, especially because of my personality type always wanting to do things perfectly/the right way.
I'm hoping this helps me pursue all of those things by simply being a healthy and happy person.

### Isn't this just like a really dumbed down workout tracker? ###
Totally.

It's not meant to be for one specific goal, but all of my goals boiled down to their most basic components. "Am I motivated"
is the biggest question I ask myself every day. Ever since my family has left I'm having a hard time feeling
any worth or contribution to society.

Sometimes it feels like even if I got a world record, made a million dollar idea come to fruition, or wrote some amazing
novel programming library I'd still feel unhappy. That's why I need to start worrying about these metrics.

Tracking
========

### Daily tracking ###
- Happy
    * 1 being seeing my mom with tubes coming out of her face and head
    * 10 being happiest I've ever been, nothing feels impossible
- Motivated
    * 1 being ultra depressed not even eating
    * 10 being I did everything I needed to and more
- Flexibility
    * 1 being no stretching in chair all day no walking around
    * 10 being I did every stretch possible and did the splits
- Strength
    * 1 being I feel as soft as an 8 year old girl
    * 10 being I squatted and deadlifted the day before--now I can't move
- Endurance
    * 1 being I got winded getting out of my chair
    * 10 being I jump roped for 10 minutes and ran a mile without breathing hard
- Relationship
    * 1 being I got into a huge argument and feel terrible
    * 10 being we made dinner together and wrote each other poetry

### Monthly tracking ###
- Life goals
    * 1 being no progress towards goals and very depressed
    * 10 being I got a world record deadlift
- Power
    * 1 being no physical activity
    * 10 being I ran and worked out every opportunity I had
- Nature
    * 1 being no outdoor activity
    * 10 being I spent the entire time camping and fishing


Implementation
========

### Usage ###
Page has 2 tabs: Output and Input

**Output page**
- A bunch of badass meters for each metric.
- Graph view of the last 30 days
- A list of notes for that current month (useful for making monthly evaluations like how many times did I go in nature)

**Input page**
- Coming to the input page you should see all of the daily metrics that still need entering.
- You should setup a Google reminder at 915PM every day to fill in these metrics.
- At the beginning of each month, monthly metrics should appear as well

### Backup ###
- Dump database daily to eric@ckcollab.com

### Models ###
**Metric**
- Name (Happy)
- Description of 1
- Description of 10

**Measurement**
- Date/time
- int 1 through 10
- Notes for this measurement if applicable


