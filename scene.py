from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("subclass it and implement enter()")
        exit(1)

class Death(Scene):

    last_breath = [
        "You died... You suck at this game.",
        "This isn't even a hard game...",
        "You disappointed yourself and your family.",
        "Sucks to suck nerd."
    ]

    def enter(self):
        print(Death.last_breath[randint(0, len(self.last_breath)-1)])
        exit(1)

class MagicForest(Scene):

    mf_options = ['look for help', 'run after the goblin', 'start screaming']

    def enter(self):
        print(dedent("""
            You and your son Mike are hiking and you stumble across a strange looking
            path. You want to stay on the same path but 5 year old Mike begs you to
            take this strange path. You begrudgingly agree, but you think to yourself
            that this path is almost calling to you.
            There's a dense fog making it hard to see. The trees seem bigger, the plant
            seem... different. everything has a slight glimmer to it.

            As you and Mike explore this new area your hear some leafs crinkle and
            twigs snap. You turn around expecting a fellow hiker but you see a green,
            man like figure standing behind you. You think your eyes are playing tricks
            on you, Mike clinches to your leg. The green thing opens it's wide mouth
            displaying rows of maggled teeth. He lets out a skin crawling laugh and
            say 'you dont belong here.' You find your stranth and say 'I dont even
            know where we are, we are lost.' The green...thing...says 'You walked
            through the portal to the magic forest.' You say in disbelief 'The magic
            forest?'. The thing does its laugh again and says 'Yes, I am Gwarp, I am
            the resident goblin. As the goblin of this forest I must take the forest
            toll.' Before you can comprehend what he said, he runs faster then any
            creature you've ever seen and grabs Mike.

            You yell 'What the FUCK, give me my son'. The goblin laughs at you and
            darts of with your son. What do you do now? Do you search for help?
            Run after the speed demon? Start screaming for help?
            """))

        print("Type \"look\" to look for help.")
        print("Type \"run\" to run after Gwarp.")
        print("Typy \"yell\" to start screaming for help.")

        print('-' * 15)

        action = input('> ').lower()

        if action == "look":
            print(dedent("""
                You start frantically looking for help! What the fuck just happened?
                you're so confused and scared. As far as you can tell no one else is
                around you. You're pleads for help go unanswered. You take a deep
                breath and compose yourelf. You start start walking in the direction
                you saw that beast take your son. You see what you think is a cabin
                or a hut through the fog. You decide to to go in.
                """))

            return 'the_cabin'


        elif action == "run":
            print(dedent("""
                You start sprinting as fast as you can in the direction that Gwarp
                ran off in. The fog is too thick, you can't see 10 feet in front of
                you. You get disorientated and confused, but you press on and keep
                running. You take another stride and realize too late that there's
                no ground beneath your foot. Your eyes open wide and your stomach
                jumps to your throat as you realize you are free falling off a giant
                cliff, it must be 100 fucking feet. Right before you make contact with
                the ground you look to the top of the cliff to see Gwarp holding Mike.
                And... Splat, you died.
                """))
            return 'death'


        else:
            print(dedent("""
                You start screaming at the top of your lungs. It seems like the steem
                from your warm breath is only adding to the fog as tears of agony
                stream from your face. Yelling 'MIKE, MIKE, MIKE! fuck fuck! GIVE
                ME MY SON BACK YOU FUCKING BASTARD!' In your panic you didnt hear
                a creature sneak up behind you until you feel a pair of cold, wet
                hand wrap around your shoulders. You slowly turn around and see a
                tall creature standing over 7ft covered in what look like dark oozing
                pus. As you try to wiggle out of the creatures grasp the thing
                effortlessly picks you up and looks at you eye to eye. The things
                eyes are blood shot red and the same pus leaks out of them, the thing
                wraps its enormous hand around your neck and violently rips your head
                off bring your spin with it.
                """))
            return 'death'


class TheCabin(Scene):

    def enter(self):
        print(dedent("""
            You walk up to the cabin, the old red paint is peeling off the side
            paneling and the windows are coated in a thick layer of dust and grime.
            Pulling the sleeve to your flannel jack over your hand you whip the
            dirt of one of the glass panels on a window and peer in. The cabin
            apears to be deserted but you still knock on the door three times
            and yell 'HELLO? anyone home?'. You hear no noices from the inside so
            you push down on the door handle and step inside. You walk as gingerly
            as you can yet every step creeks against the floor seeming to echo
            into the depths of the home. The cabin looks empty as you pass room
            to room. There is a door in the kitchen that you open, you see a
            wooden staircase leading to a dirt basement the seems cold and damp.
            You reach into your pocket and pull out a small bic lighter and flick
            it and descend into the bacement. You squint to take advanage of every
            bit of light the lighter is putting off but nothing seems to be down here.
            As you start to head back to the stairs the door to the kitchen slambs
            shut. You run up the stairs and start pounding on the door. You see
            a lock on the door that you sware was not there before. As you are
            looking at the lock you hear a noice behind you and you turn to a
            man standing at the bottom of the stairs. This is like no man you've
            seen before. This man has no face, just one pale mouth that looks like
            all the blood in it had drain from it long ago. The man says to you
            'You can try 10 times to open the lock. If you can not get the lock
            to open then your soul is mine.'
            The code will be three digit and each digit will be a number 1 - 9.
            The thing says \"I will give you a hint, if 666 is the most unholy
            of numbers then you have to use the most holy number to save your
            soul.\"
        """))

        code = '777'
        guess = input("[lock]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("Incorrect!")
            guesses += 1
            guess = input("[lock]> ")

        if guess == code:
            print(dedent("""
                The lock clicks open and you push open the door. Before you slam
                the door shut you sneak a look behind you and see the man melt
                into the dirt floor. You say 'I need to get the fuck out of this
                place.' You run out the back door, back into the foggy forest
                and you see a shed. Thinking that today could not get weirder
                you run into the shed to look for anything that can help you get
                Mike back.
             """))
            return 'the_shed'

        else:
            print(dedent("""
                You fumbled around on the lock and fail to open it. After your
                10th attempt you tremor and look behind you. The man is standing
                still but his arms are extending and growing inch by inch to you.
                You're backed against the door as his arms wrap arond you and
                lifts you down the stairs as you are squirm to escape. He bring
                you in until your face is an inch from his mouth that he then opens
                wide. A black stream of energy flows from his mouth and into yours.
                You realize that he is draining your soul from you body. You see
                your body fall to the floor but you're not in it. The man vomits
                your soul into a glass jar and buries you into the dirt floor.
                All you know now is that you failed and all you will get until
                the end of time is dark damp dirt around your jar.
            """))
            return 'death'


class TheShed(Scene):

    def enter(self):
        print(dedent("""
            The door hinge creaks loudly as you fling it open as if it has not
            opened for years. You walk inside expecting some sort of disgusting
            creature. You blow a breath of relief to find you are alone. You
            spot some items that could be useful to you. You see an axe, a gas
            can full of gas, a chainsaw and some sort of rifle. You only want to
            take one of these items with you because you don't want to slow
            yourself down as you search for Mike.
            Do you take the axe? Do you take the gas? Do you take the chainsaw?
            Or do you take the rifle?
        """))

        print('-' * 15)
        print("Type in \'axe\' to take the axe.")
        print("Type \'gas\' to take the gas.")
        print("Type \'chainsaw\' to take the cainsaw.")
        print("Type \'rifle\' to take the rifle.")

        action = input('> ')

        print('-' * 15)

        try:
            if action == 'chainsaw':
                print(dedent("""
                    You grab the chainsaw but it feels light so you shake it a
                    few times and realize it's out gas. You grab the gas can to
                    fill up the chainsaw and find a map beneath can. You fill up
                    the chainsaw and pull the starter string to see if it works,
                    the chainsaw fires right up. You take a moment to study the
                    map and find where you think you are at. You also see a spot
                    marked as Gwarps dungeon. You smile to yourself as you set
                    of in the direction to the dungeon. Under your breath you say
                    \"Im coming for you fucker\".
                 """))

                return 'dungeon'

            elif action == 'axe':
                print(dedent("""
                    You decide to take arguably the least deadly weapon, the axe.
                    Stepping out to the shed you think \'okay... where to now\'.
                    You start searching for Mike heading in the direction you
                    think is North. A day goes by and you're completely lost.
                    As you walk around you keep yelling \'Mike, Mike\'. You're
                    thirsty, hungry and so scared. You stop at a creek to get
                    some water and you spot a deer like animal. You need food so
                    you start sneaking up on the creature. You're almost within
                    striking distance, you raise the axe above your head. The
                    ceature turns around and you see its face, a nightmare. Long
                    tentacles protrude from a snout much like a crocodile. In
                    shock you bring the axe down with all your strength and bury
                    the axe-head into the skull of the creature. You think \'phew
                    I really didn't want to fight that fucker\'. As you try to
                    get the axehead out to the creatures ruined skull you notice
                    8 no 12 pairs of glowing eyes observing you. 6 huge deer
                    monsters creep out of the fog, these are much bigger than the
                    one you killed, you must have killed the baby. The animals
                    charge you and rip you limb from limb.
                 """))

                return 'death'

            elif action == 'gas':
                print(dedent("""
                    You pick up the gas can and find a map under it. You quickly
                    find the shed on the map and then you see it... A marked
                    spot that says Gwarps dungeon. You set off for Gwarps dungeon
                    gas can in hand. You get to the dungeon and see Mike inside,
                    you start pouring gas around the perimeter of the dungeon.
                    as soon as the gas is mostly out you barge inside. The place
                    is a horror show but you ignore the hellscape that surrounds
                    you and you run to a cage that has Mike inside. You kick off
                    the lock and grab Mike. Gwarp is standing at the door with
                    a shocked look and his mangled face, he say \'I dont understand
                    how you found me but now I get to feast on two people\'. You
                    say angrily \'eat this\' as you throw the remaining gas on him.
                    with a smile you take out your lighter and set the little fucker
                    on fire. You immediately realize your mistake. The whole place
                    catches fire. You start carring make towrds the door but its
                    totally engulfed in flames. Your feet start to catch fire where
                    some gas leaked onto them. You and Mike burn to death in
                    the dungeon of nightmares.
                """))
                return 'death'

            else:
                print(dedent("""
                    You grab the rifle and run out of the shed. You\'ve never
                    been much of a shot but you figure you\'ll be able to blast
                    the shit out of Gwarp. You start heading in the direction that
                    you think is south. A about 8 hours into searching for Mike
                    you see a... no it cant be... yes... a centaur. This beast is
                    half horse half man. You appraise the centaur and it doesnt
                    look evil but with the day you\'re having you\'re not about
                    to trust anything. You aim your rifle at the centaur and pull
                    the trigger. CLICK. Oh shit you did\'t check to see if you
                    had bullets. The clicking of the gun alerts the centaur who
                    turns around to see you aiming a gun at him. He snarls and
                    says \'did you just try to fucking kill me\'. Before you can
                    respond the centaur charges you and staples your body until
                    your less of a person and more of a jelly.
                """))
                return 'death'

        except:
            print("Not a valid answer please try again.")
            TheShed()



class Dungeon(Scene):

    def enter(self):
        print(dedent("""
            You follow the map and find Gwarps Dungeon. No other creatures fucked
            with you during your travels to the Dungeon, you equate that to the
            menacing look on your face. You sneek up to the Dungeon thats carved
            into the base of a mountain. Theres one wooden door separating you
            from the inside of Gwarps Dungeon. You slowly open the door...
            You see Mike in the back locked in a metal cage, in the center of the
            room theres a cauldron with a fierce fire roaring below it. You keep
            looking and you dont see Gwarp. Do you run in and kick open the cage
            to let Mike out? or do you explore the dungeon to look for Gwarp?
        """))
        print('-' * 15)

        print("Type \'cage\' to let Mike out.")
        print("Type \'gwarp\' to look for Gwarp first.")

        action = input('> ').lower()

        try:
            if action == 'cage':
                print(dedent("""
                    You know you should look for Gwarp but you can\'t stand to
                    see Mike in that cage for a second longer. You run over and
                    Mike turns to you and yells \"DADDY!\" The cage looks old and
                    rickety so you chance kicking the door off. You give it three
                    strong kicks and boom! the door flys open! The Hawk family is
                    reunited! You start running to the door with Mike hidden behind
                    you... All the sudden the front door opens up and Gwarp is
                    standing there. He looks at you with a look of shock and
                    bewilderment. Gwarp does is skin crawling laugh and says
                    \"I have to hand it to you, I thought you\'d be dead by now.
                    I guess I have two people to feast on.\" He dashes over to you
                    with the seep of a cheetah and grabs you by the throat with both
                    hands and lifts you off the ground. You start kicking and gasping
                    for air but in a moment of clarity you remember the chainsaw
                    in your hand. You pull the ignition string and the chainsaw
                    starts right up. Gwarp glances down as you bring the chainsaw
                    up underneath his legs. You start sawing him in half from
                    the asshole up, Gwarp is letting out a ear blistering cry
                    until you reach his throat. You bring the chainsaw through
                    his head and lift the chainsaw over your head as the two halfs
                    of Gwarp fall in opposite directions. You turn around and
                    hug Mike and say \"I love you so much Mike Hawk, I'll never
                    let Mike Hawk go again\" You dont know how you are going to
                    get out of the Magic Forest but you know as long has you have
                    little Mike Hawk things will be okay.
                """))
                return 'finished'

            else:
                print(dedent("""
                You go inside and start looking for Gwarp. Mike sees you and
                starts yelling \"DADDY!\". You put your finger over your mouth to
                tell him to quiet down. You don't see Gwarp anywhere you move to
                the next room over. You open the door and immediately get punched
                in the dick. You bend over in agonizing pain, you drop you
                chainsaw to grab your balls. Tearful eyes look up to see Gwarp
                he laughs that devilish laugh and says \"I don\'t know how your
                alive, but no worry you wont be for long!\" He punches you in the
                face and you blackout. You wake up hanging  by your feet as Gwarp
                walks over to you with a rusty knife. He said \"This is going
                to really hurt\" and then does his laugh again. He starts hacking
                off you limps with is dull knife after your second arm goes you
                blackout from blood loss and never wake again.
                """))
                return 'death'

        except:
            print("Not a valid answer please try again.")
            Dungeon()


class Finished(Scene):

    def enter(slef):
        print("You won! Great work, I didn't think it would happen but you did it!")
        return 'finished'
