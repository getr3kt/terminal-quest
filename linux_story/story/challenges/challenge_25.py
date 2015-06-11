#!/usr/bin/env python
#
# Copyright (C) 2014, 2015 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU General Public License v2
#
# A chapter of the story


from linux_story.story.terminals.terminal_mkdir import TerminalMkdir
from linux_story.story.challenges.challenge_26 import Step1 as NextChallengeStep
from linux_story.step_helper_functions import unblock_commands_with_cd_hint


class StepTemplateMkdir(TerminalMkdir):
    challenge_number = 25


class Step1(StepTemplateMkdir):
    story = [
        "Bernard: {{Bb:Hello! Shush, don't say a word.}}",

        "{{Bb:I know why you're here. You want a shed!",

        "I have just the thing for you. I have the}} "
        "{{lb:best-shed-maker-in-the-world.sh}}",

        "\nHe seems pretty enthusiastic about it. {{lb:Examine}} the tool "
        "{{lb:best-shed-maker-in-the-world.sh}}",

        "\n{{gb:Use TAB to speed up your typing.}}"
    ]

    start_dir = "~/town/east-part/shed-shop"
    end_dir = "~/town/east-part/shed-shop"

    hints = [
        "{{rb:Use}} {{lb:cat}} {{rb:to examine the}} "
        "{{lb:best-shed-maker-in-the-world.sh}}",

        "{{rb:Use}} {{yb:cat best-shed-maker-in-the-world.sh}} "
        "{{rb:to examine the tool.}}"
    ]

    commands = [
        "cat best-shed-maker-in-the-world.sh",
        "cat ./best-shed-maker-in-the-world.sh"
    ]

    def next(self):
        Step2()


class Step2(StepTemplateMkdir):
    story = [
        "Bernard: {{Bb:It's like magic!  Just run the command, "
        "and you get a new shed.}}",

        "We recognise the contents...it's just the command {{lb:mkdir}} "
        "that we learnt before.",

        "Bernard: {{Bb:Try it out! Use it with}} "
        "{{yb:./best-shed-maker-in-the-world.sh}}",

        "\n{{gb:Use TAB to speed up your typing.}}"
    ]

    start_dir = "~/town/east-part/shed-shop"
    end_dir = "~/town/east-part/shed-shop"

    hints = [
        "{{rb:Do as Bernard says - use}} {{yb:./shed-maker}} "
        "{{yb:to run his script}}"
    ]
    commands = [
        "./best-shed-maker-in-the-world.sh"
    ]

    def next(self):
        Step3()


class Step3(StepTemplateMkdir):
    story = [
        "Look around to see if it created a shed."
    ]
    start_dir = "~/town/east-part/shed-shop"
    end_dir = "~/town/east-part/shed-shop"
    commands = [
        "ls",
        "ls -a"
    ]
    hints = [
        "{{rb:Use}} {{yb:ls}} {{rb:to look around yourself.}}"
    ]

    def next(self):
        Step4()


class Step4(StepTemplateMkdir):
    story = [
        "It worked! You can see a new shed in the room.",
        "What happens if you run it again?",
        "{{gb:Press UP twice to replay the old command.}}"
    ]

    start_dir = "~/town/east-part/shed-shop"
    end_dir = "~/town/east-part/shed-shop"

    hints = [
        "{{rb:See what happens when you run the script again.}}",

        "{{rb:Run the script again using}} "
        "{{yb:./best-shed-maker-in-the-world.sh}} "
        "{{rb:to see what happens.}}"
    ]
    commands = [
        "./best-shed-maker-in-the-world.sh"
    ]

    def next(self):
        Step5()


class Step5(StepTemplateMkdir):
    story = [
        "Bernard: {{Bb:Of course it won't work second time - "
        "you already have a shed!",

        "I'm working on the next big thing,}} {{lb:best-horn-in-the-world.sh}}. "
        "{{Bb:It can be used to alert anyone that you're coming. "
        "I'm having some teething problems with it, "
        "but I'm sure I'll fix it soon.}}",

        "\n{{lb:Examine}} {{lb:best-horn-in-the-world.sh}} and see if you "
        "can identify the problem.",

        "{{gb:Remember to use TAB!}}"
    ]

    start_dir = "~/town/east-part/shed-shop"
    end_dir = "~/town/east-part/shed-shop"
    commands = [
        "cat best-horn-in-the-world.sh"
    ]

    hints = [
        "{{rb:Use}} {{lb:cat}} {{rb:to examine the tool.}}",
        "{{rb:Use}} {{yb:cat best-horn-in-the-world.sh}} {{rb:to examine the "
        "tool.}}"
    ]

    def next(self):
        Step6()


class Step6(StepTemplateMkdir):
    story = [
        "The tool reads {{yb:eco \"Honk!\"}}",
        "That looks a lot like {{lb:echo}}...we could probably fix this tool!",
        "How could we make changes to this tool?",
        "\nBruno: {{Bb:Ho ho, you look like you understand the problem.}}",
        "Eleanor: {{Bb:If we need extra information, we can go look in the "
        "library.}}"
        "{{Bb:It was just outside.}}",
        "\nBefore we go, have a look in the {{lb:secret-room}}."
    ]

    start_dir = "~/town/east-part/shed-shop"
    end_dir = "~/town/east-part/shed-shop"

    commands = [
        "ls secret-room",
        "ls secret-room/",
        "ls -a secret-room",
        "ls -a secret-room/",
    ]

    hints = [
        "{{rb:Use}} {{yb:ls}} {{rb:to look through.}}",
        "{{rb:Use}} {{yb:ls secret-room/}} to look inside."
    ]

    def next(self):
        Step7()


class Step7(StepTemplateMkdir):
    story = [
        "Bernard: {{Bb:Oooh naughty, you can't go in there.}}",
        "\nLet's leave the shed shop and find the library."
    ]

    start_dir = "~/town/east-part/shed-shop"
    end_dir = "~/town/east-part"
    commands = [
        "cd ../",
        "cd .."
    ]
    hints = [
        "{{rb:Leave the shed-shop using}} {{yb:cd ../}}"
    ]

    last_step = True

    def block_command(self):
        return unblock_commands_with_cd_hint(
            self.last_user_input, self.commands
        )

    def next(self):
        NextChallengeStep(self.xp)
