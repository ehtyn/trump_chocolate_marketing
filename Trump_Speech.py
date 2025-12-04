from gtts import gTTS


# Prompts to say
complainer = gTTS("Kids love it. Moms love it. Even that guy who complains about everything — he loves it. Can’t stop drinking.")
other_people = gTTS("Folks, it’s the hottest hot chocolate. People taste it and they go, ‘Wow.’ Nobody’s ever seen cocoa like this.")
other_cocoa = gTTS("Other cocoa? It’s weak. Very weak. This cocoa? Strong. Tremendous strength in the cup.")
one_sip = gTTS("You take one sip and suddenly your whole day — it’s better. You feel like a winner again.")
real_chocolate = gTTS("We use real chocolate. Not the fake stuff. Not the powdered disaster. Real. Beautiful. Chocolate.")
marshmallows = gTTS("You want marshmallows? We’ve got marshmallows. Huge ones. The best. They float like little golden boats.")
believe_me = gTTS("Believe me, its the best. Thick, creamy, not the loser stuff. ")
I_Know = gTTS("I know what I’m talking about, I’ve tasted a lot of cocoa. This is the one.")
People_always_say = gTTS("People always say, ‘How can hot chocolate be this good?’ And I tell them — it just is.")
its_true = gTTS("It’s true, we make it the real way. None of that weak, watered-down stuff.")
the_best = gTTS("The best, the very best. Creamy, rich, absolutely perfect.")
good_cocoa = gTTS("I know what you’re thinking: ‘Can hot chocolate really be this good?’ The answer is yes. Absolutely yes.")
we_do_right = gTTS("It’s true, we do things right. That’s why everybody’s talking about it.")


# Creates and saves voices
complainer.save('complainer.mp3')
other_people.save('other_people.mp3')
other_cocoa.save('other_cocoa.mp3')
one_sip.save('one_sip.mp3')
real_chocolate.save('one_sip.mp3')
marshmallows.save('marshmallows.mp3')
believe_me.save('believe_me.mp3')
I_Know.save('I_Know.mp3')
People_always_say.save('People_always_say.mp3')
its_true.save('its_true.mp3')
the_best.save('the_best.mp3')
good_cocoa.save('good_cocoa.mp3')
we_do_right.save('we_do_right.mp3')

print('Completed and saved all voices. ')