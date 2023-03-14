# AUTOMATIC GTD MANAGER

As a [GTD](https://es.wikipedia.org/wiki/Getting_Things_Done) adherent who has experienced issues with life management, I believe that Notion is a powerful tool for creating a life management framework, but its approach can result in a framework that is too complex to handle realistically. Therefore, I aim to create a simpler GTD-based CLI tool to simplify project administration


Content:

- [GTD Approach implemented](#gtd-approach-implemented)
- [Project's life stage](#project-life-stage)
- [Main features](#main-features-to-be-delivered-the-first)
- [Should you use this?](#should-you-use-this)
- [How to use](#how-to-use)

## GTD approach implemented

Main sources are original GTD book from David Allen, and i'm often inspired by the GTD vision of José Miguel Bolivar (Optima Infinito)

### Project's gtd's values:

- Computerized storage over brain storage
- Efficacy with efficiency over pure Efficacy
- Reflection and organization over chaos
- Long-term maintainability over efficacy
- Decomposition of complexity over occasional hard work.

### GTD approach

This project implements such a own way of GTD methodology:

#### System Reviews

- Long reviews use to be a mental beating

GTD can result in long lists that are difficult to maintain. It's important to review these lists with a frequency that aligns with their impact on your higher objectives to maintain efficacy. However, having endless lists makes it challenging. We must acknowledge the priority hierarchy in our lives and determine when, what, and how to review. My proposal is to define priority types and set different review periods for each type, including low, medium, and high priority of revision.

- Weekly reviews are often mentally hard

This clashes directly with the concept of operational efficiency sought by gtd, given that, only after a lot of hard thinking at high levels of vision, we focus on the "day-to-day" level.

At now, we can find that our one "weekly" revision broke down, in at least 3 simpler and quicker reviews: for low, medium and high levels of worth, we gonna do casual, frequent and constant reviews, respectively.

We can find that, in the official methodology, weekly revision is a project-based revision. And that has the aim to keep our mind in a "low picture level" through the day-to-day level, and being able to "take a step up" over the dayly tasks reviewing, to readjust and redefine our projects and actions.

My proposal is about *split weekly revision in at least 2 block-of-work sessions* in which we are going to go up-down in our system. I like the Bolivar's proposition to "do a up-to-date review, and then do a "future-vision" review"

Abstract: 
1. We gonna prioritize things to be review, depending on how much value it brings to our higher-level perspective objectives.
2. Initially, we can find three levels of priority: low, medium and high.
3. Weekly review is about projects and its tasks.
4. Weekly review is splitted in 2 blocks temporarily close: updating and preparing.

#### Execute step

In the Execute step, or "do" step however, it's our responsibility to select what we gonna do now. 
System Effectivity depends on the previous steps, here there's nothing to do about it. 

Once we got it, we can going on over *how to choose what to be done*.

You should know there's 3 types of work in gtd: Working on emergent inputs, Working on defined things, and working on define inputs (clarify over your inbox).

If you're temporarily free, you want to choose what type of work to do. 

1. If your choice is to work on what has already been defined, you should follow this iterative path:
  a) Check your calendar.
  b) Check lists:
    I. Available contexts right now.
    II. Available agendas right now.
    III. Checklists
  c) Delimite: First, how much time you got now? Second, how much energy you got now? Third, how high a priority is the task?

2. If your choice is to define inputs (Clarify so) then you want follow this iterative path:
  a) Analyze it (what does it mean for you?)
  b) Decide what you have to do with it 
    I. Does this require to take action? (If it doesn't, you should delete it, archive it or keep it on standby)
    II. In the positive case, there is more than 1 task to be done, or it's only 1?
    III. You gonna start organizing tasks of a *project* if there're multiple tasks. 

At this point, you start to go on [organize tasks](#organize-tasks). It's crucial to realize that, if you got a project, you must do the organize step iteratively over each project's action.
If there will be more than 1 action, you should get a reminder, in gtd it's called as "project".
If there wont be more than 1 action, you should organize that action without any project declaration.

Anyway, in both cases, inbox is cleared.

#### Organize tasks

In gtd, tasks are organized in this way:

1. Can you do this in less than 2 minutes? -> do it.
2. Can YOU do this, or you should delegate it? 
- If your choice is to delegate, you should keep a reminder of this in the "following" list.
- If your choice is to not delegate, you should decide if it has a time stop of it hasn't.
  - If it does, you must add it to your calendar.
  - If it doesn't, you must add it to your "next actions" to be done as soon as possible.

## Project's life stage

==This is on pre-alpha. Main features are not availables yet==

## Main features to be delivered the first

I'm working on these set of features...
  1. CRUD of tasks, projects, life resp areas, goals, vision and life-vision.
  2. Division in what info you see related to projects and tasks, depending on what are you doing
  * if you are working, you should only see info about next actions, reference resources and so..
  * if you are reflecting, you should only see info about tasks dependencies trees, projects status, workload, etc
  3. Separated frameworks on the gtd 5 steps: Collect, Task-managing, Tasks-Organization, Tasks-review, and Do
  4. An easy touch inbox, focussed on get free your brain.

## Should you use this?

If you're like me: 
  1. You appreciate simple but well defined tools 
  2. You often go on cli 
  3. You tends to complex your projects
  4. You appreciate to see things in perspective when things takes it.
... so, sure you want to try this.
Nothing like use a tool created by similar people...

If you appreciate complexity on task managing, or you want to work in a more "chaotic" way, i strong do not suggest for you to use this.

## How to use
...





