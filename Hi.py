import asyncio

import time

from asyncio import Queue, TaskGroup, sleep

from itertools import count

from typing import (TYPE_CHECKING, Any, Callable, ClassVar, Literal, Protocol,

                    TypeAlias, TypeVar)

from aiohttp import ClientWebSocketResponse

from attrs import Factory, define                                                               from highrise import (BaseBot, ChatEvent, Highrise, UserJoinedEvent,

                      UserLeftEvent)

from highrise.models import (AnchorPosition, ChannelEvent, ChannelRequest,                                                   ChatEvent, ChatRequest, CurrencyItem, EmoteEvent,

                             EmoteRequest, Error, FloorHitRequest,

                             GetRoomUsersRequest, GetWalletRequest,

                             IndicatorRequest, Item, Position, Reaction,                                                     ReactionEvent, ReactionRequest, SessionMetadata,

                             TeleportRequest, TipReactionEvent, User,

                             UserJoinedEvent, UserLeftEvent)

import random                                                                                   lop = ["تحت العبايه حكايه😉🤍", "اي يا ملاكي دا انتي الملاكي 😍💃", "اجمل حد قابلتو😉🤍", "هو نت في زيك😉❤️", "يريتني كنت التوكتك😂❤️", "خليني اشوفك دايما بفرح🤓🤍", "قاسي وحارح احساسي😉❤️💃", "يا دنيا ميلي ميلي انت الي باقيلي 😉❤️🤙", "احلا حته😉❤️✨"]

dancs = ["idle-loop-sitfloor", "emote-tired", "emoji-thumbsup", "emoji-angry", "dance-macarena", "emote-hello", "dance-weird", "emote-superpose", "emote-suckthumb", "emote-peace", "emote-exasperated", "idle-loop-happy", "idle-loop-annoyed", "idle-lookup", "idle-hero", "emote-wings", "emote-judochop", "emote-rainbow", "emote-robot", "emote-laughing", "emote-kiss", "emote-wave", "emote-hearteyes", "emote-exasperatedb", "emote-jumpb", "emote-dab", "idle-loop-sad", "emote-theatrical", "emote-teleporting", "emote-slap", "emote-ropepull", "emote-graceful", "idle-dance-headbobbing", "emote-think", "emote-proposing", "emote-peekaboo", "emote-kicking", "emote-jetpack", "emote-hot", "emote-heartshape", "dance-shoppingcart", "emote-heartfingers", "emote-greedy", "emote-frustrated", "emote-float", "emote-fainting", "emote-embarrassed", "emote-cold", "emote-baseball", "dance-sexy", "emoji-smirking", "emoji-sick", "emoji-scared", "emoji-punch", "emoji-mind-blown", "emoji-hadoken", "emoji-give-up", "emoji-eyeroll", "emote-yes", "idle_singing", "sit-idle-cute", "idle_layingdown2", "idle-floorsleeping2", "idle-floorsleeping", "idle-enthusiastic", "emote-hug", "emote-confused", "emoji-lying", "emoji-dizzy", "emoji-celebrate", "dance-zombie", "dance-singleladies", "emote-no", "emote-swordfight", "emoji-clapping", "emote-happy", "emote-shy", "dance-tiktok2", "emote-model", "dance-breakdance", "dance-floss", "emote-charging", "emote-snake", "emote-gangnam", "dance-russian", "emote-sad", "emote-lust", "emoji-cursing", "emoji-flex", "emoji-gagging", "dance-tiktok8", "dance-blackpink", "dance-pennywise", "emote-bow", "emote-curtsy", "emote-snowball", "emote-snowangel", "emote-telekinesis", "emote-maniac", "emote-energyball", "emote-frog", "emote-cute", "dance-tiktok9", "dance-tiktok10", "emote-pose7", "emote-pose8", "idle-dance-casual", "emote-pose1", "emote-pose3", "emote-pose5", "emote-cutey" ]

class MyBot(BaseBot):

                                                                                                    async def on_start(self, session_metadata: SessionMetadata) -> None:

        try:

            await self.highrise.walk_to(Position(16,0,25,'FrontRight'))

        except:                                                                                             print("error 3")

                                                                                                    async def on_user_join(self, user: User) -> None:

        if user.username == "_AnGeL_l" :

            try:

                await bot.follow("dead_code")                                                     #              await self.highrise.chat(f'الكبير وصل يرجالة رحبوا بي الغزال ')

   #             await self.highrise.chat(f'⚠️⚠️⚠️⚠️⚠️⚠️')

    #            time.sleep(2)

            except:

                print("ji")

        try:

            await self.highrise.send_emote('emote-happy')

            value = random.choice(lop)

            await self.highrise.chat(f'{value} {user.username}')

        except:                                                                                             print("error 3")

                                                                                                    async def on_chat(self, user: User, message: str) -> None:

        if message.startswith("نزلني"):

            try:                                                                                                await self.highrise.teleport(f"{user.id}", Position(10,0,22))

            except:

                print("error 3")

#        if message.startswith("فلور"):

 #           try:

  #              emote_id = "dance-floss"                                                          #             await self.highrise.send_emote(emote_id, user.id)

    #        except:

     #           print("error 3")

                                                                                                

#        while True:

 #           if message.startswith("رقصني"):

  #              try:                                                                              #                 emote_id = random.choice(dancs)

    #                await self.highrise.send_emote(emote_id, user.id)

     #           except:

      #              print(f"{emote_id}")                                                           # يمكن وضع المزيد من الشروط هنا

       #     await asyncio.sleep(3)

                                                                                                

        if message.startswith("رقصني"):

            try:                                                                                                emote_id = random.choice(dancs)

                await self.highrise.send_emote(emote_id, user.id)

            except:

                print(f"{emote_id}")

                                                                                                

#        if message.startswith("قديش معك") :

 #           wallet = (await self.highrise.get_wallet()).content                                  #          await self.highrise.chat (f"معايا بس  {wallet [0].amount} قولد زيدني شوي مبخلك ")

                                                                                                        if message.startswith('مكانك بوت 1') :

            if user.username == "_AnGeL_l" or user.username == "aleen._" or user.username == "_EGhazal_" or user.username == "dead_code" :

                try:                                                                                                await self.highrise.chat(f"حاضر يا غزال")

                    await self.highrise.walk_to(Position(16,0,21,'FrontRight'))

                except:

                    print("error 1")                                                            

                                                                                                #        while True:

 #           message = # get message

#            user = # get user

 #           if message.startswith('تعال بوت 1') :                                                #              if user.username == "" or user.username == "dead_code" or user.username == "_AnGeL_l" :

   #                 try:                                                                           #                    response = await self.highrise.get_room_users()

     #                   users = [content[0]

      #                           for content in response.content]

       #                 usernames = [user.username.lower()

        #                             for user in users]  # Extract the usernames

         #               parts = message[1:].split()

          #              args = parts[1:]                                                                  #             print(args[0][1:])

            #            username = args[0][1:] # اسم المستخدم الذي تريد الحصول على قيمته

                # تحديد اسم المستخدم الذي تريد العثور على موقعه (position)                      #                        target_username = user.username

                # البحث عن موقع (position) للمستخدم (User) المحدد

 #                       for user, position in response.content:                                  #                          try:

   #                             if user.username == target_username:

    #                                print(position)

     #                               x = position.x                                                   #                              y = position.y

       #                             z = position.z

        #                           facing = position.facing

         #                          await self.highrise.chat('جيتك زعيممم')                               #                          await self.highrise.walk_to(Position(x-1,y,z-1, facing))

            #                except:

           #                     print("error 1")

             #       except:

              #          print("error 1")

                                                                                                

        if message.startswith('تعال بوت 1') :

            if user.username == "" or user.username == "" or user.username == "_AnGeL_l" or user.username == "_EGhazal_" or user.username == "dead_code" :                                                      try:

                    response = await self.highrise.get_room_users()

                    users = [content[0]                                                                                      for content in response.content]

                    usernames = [user.username.lower()

                                 for user in users]  # Extract the usernames

                    parts = message[1:].split()

                    args = parts[1:]

                    print(args[0][1:])                                                                              username = args[0][1:] # اسم المستخدم الذي تريد الحصول على قيمته

                # تحديد اسم المستخدم الذي تريد العثور على موقعه (position)

                    target_username = user.username                                             

# البحث عن موقع (position) للمستخدم (User) المحدد

                    for user, position in response.content:

                        try:                                                                                                if user.username == target_username:

                                print(position)

                                x = position.x

                                y = position.y                                                                                  z = position.z

                                facing = position.facing

                                await self.highrise.chat('جيتك زعيممم')

                                while True:                                                                                         await self.highrise.walk_to(Position(x-1,y,z-1, facing))

                        except:

                            print("error 1")

                                                                                                                except:

                    print("error 1")

        if message.startswith('طيرني') or message.startswith('fly') :

            try:

                kl = Position(random.randint(1, 19), random.randint(1, 15), random.randint(1, 19))

                await self.highrise.teleport(f"{user.id}", kl)

            except:                                                                                             print("error 3")

#        if message.startswith('مراجيح') and user.username == "_AnGeL_l" or message.startswith('مراجيح') and user.username == "dead_code" :                                                      #           try:

  #              response = await self.highrise.get_room_users()

   #             print(response)

    #            users = [content[0]                                                                 #                    for content in response.content]  # Extract the User objects

      #          id = [user.id.lower()

       #               for user in users]  # Extract the usernames

        #        exclude_user0id = "643adf8aae71adf6177b6928"                                            #       print(id)

          #      for i, user0id in enumerate(id):

           #         if user0id != exclude_user0id :

            #            try:                                                                                #               kl = Position(random.randint(1, 19), random.randint(1, 15), random.randint(1, 19))

              #              print(type(kl))

               #             await self.highrise.teleport(f"{user0id}", kl)                                     #        except:

                 #           print("error 1")

                  #  else :

                   #     print("error 4")                                                                   #except:

             #   print("error 2")

    async def on_whisper(self, user: User, message: str) -> None:                                #       emote_dance = ["emote-float", "dance-blackpink", "emote-disco", "emote-swordfight", "emote-gordonshuffle", "emote-handstand"]

  #      if message.startswith('Rest') :

   #         try:

    #            emote_id = "sit-idle-cute"

     #           response = await self.highrise.get_room_users()

      #          users = [content[0] for content in response.content] # extract t>                     #         userIds = [user.id for user in users] # extract the user IDs

#

 #               for id in userIds:

  #                  await self.highrise.send_emote(emote_id, id)                                  #         except:

    #            print("error 3")

     #   if message.startswith('شعلها') :

      #      try:                                                                               

#

 #               emote_id = random.choice(dancs)

  #              response = await self.highrise.get_room_users()                                   #             users = [content[0] for content in response.content] # extract the user objects

    #            userIds = [user.id for user in users] # extract the user IDs

#

 #               for id in userIds:                                                               #                  await self.highrise.send_emote(emote_id, id)

   #         except:

    #            print("error 3")

        try:

            if message.lstrip().startswith('اطرد') and user.username == "dead_code":

                response = await self.highrise.get_room_users()

                users = [content[0] for content in response.content] # extract the user objects

                usernames = [user.username.lower() for user in users] # extract the usernames                   parts = message[1:].split()

                args = parts[1:]

                if len(args) < 1:                                                                                   await self.highrise.send_whisper(user.id, "Usage: اطرد <@username>")

                    return

                elif args[0][0] != "@":                                                                             await self.highrise.send_whisper(user.id, f"Invalid user format. Please use '@username'.")

                    return

                elif args[0][1:].lower() not in usernames:

                    await self.highrise.send_whisper(user.id, f"{args[0][1:]} is not in the room.")                                                                                                                 return

                user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)                                                                                                        if not user_id:

                    await self.highrise.send_whisper(user.id, f"User {args[0][1:]} not found")

                    return

                                                                                                                await self.highrise.moderate_room(user_id, "kick")

        except:

            print("error 3")

#        try:                                                                                    #           await self.highrise.send_whisper(f"637684b031fd5d1811bcf850", f"@{user.username} :- {message}")

  #      except:

   #         print("error 3")                                                                           if message.startswith('تت') and user.username == "_AnGeL_l" or message.startswith('تت') and user.username == "dead_code":

            try:

                xxx = message[2:]                                                                               await self.highrise.chat(xxx)

            except:

                print("error 3")

###$####$####$####$####$####$####$####$####$####$####$####$####$####$####$####$####$####$#

#        if message.lstrip().startswith('نن'):

 #           try:

  #              response = await self.highrise.get_room_users()

   #             users = [content[0]                                                                #                     for content in response.content]

     #           usernames = [user.username.lower()

      #                       for user in users]  # Extract the usernames                              #         parts = message[1:].split()

        #        args = parts[1:]

#                print(args[0][1:])

 #               username = args[0][1:] # اسم المستخدم الذي تريد الحصول على قيمته               #

 #               # تحديد اسم المستخدم الذي تريد العثور على موقعه (position)

  #              target_username = args[0][1:]

                                                                                                # البحث عن موقع (position) للمستخدم (User) المحدد

#                for user, position in response.content:

 #                   try:

  #                      if user.username == target_username:                                      #                         print(position)

    #                        x = position.x

     #                       y = position.y

       #                     z = position.z                                                           #                      facing = position.facing

        #                    kkk = message.split()

         #                   mm = "تجريب بالغش"

#                                                                                                #                           await self.highrise.walk_to(Position(x-1,y,z-1, facing))

  #                          return

   #                         await self.highrise.chat(f'{mm}')                                      #                        return

     #                       print(type(x))

##

  #                          new_position = {"x": x, "y": y, "z": z, "facing": facing}

#                                                                                                ##                           print(new_position)

#

  #                  except:

   #                     print("tshe tshe 2")                                                   

    #        except:

     #           print("tshe tshe")

###$####$####$####$####$####$####$####$####$####$####$####$####$####$####$####$#>               

#        try:

 #           if message.lstrip().startswith('قلب'): #change the command name here

  #              try:                                                                           #

 #                   if user.username  == "_AnGeL_l" or user.username  == "dead_code" :

  #                      response = await self.highrise.get_room_users()

   #                     print("this respose --- ", response)                                       #                    users = [content[0]

     #                            for content in response.content]  # Extract the User objects

      #                  print("this users ------", users)

       #                 usernames = [user.username.lower()

        #                             for user in users]  # Extract the usernames

         #               print("this username----", usernames)

          #              parts = message[1:].split()

           #             print("this parts----", parts)

            ##            args = parts[1:]

              #          print("this arges -----", args)                                                       #         user_id = next(

                #            (u.id for u in users if u.username.lower() == args[0][1:].lower()), None)

                 #       print(user_id)                                                                           #      await self.highrise.react("heart",user_id)

#                except:

 #                   pirnt("9999")                                                              

#            if message.lstrip().startswith('pp'): #change the command name here                 #               if user.username  == "_AnGeL_l" or user.username  == "dead_code" : # to add specifi

#

 #                   response = await self.highrise.get_room_users()                              #                  users = [content[0]

   #                          for content in response.content]  # Extract the User objects

    #               usernames = [user.username.lower()

      #                           for user in users]  # Extract the usernames                          #             parts = message[1:].split()

        #            args = parts[1:]

         #           user_id = next(

          #              (u.id for u in users if u.username.lower() == args[0][1:].lower()), None)

           #         if len(args) < 2:

            #            await self.highrise.send_whisper(user.id, "Usage: pp <@username> <position>")                                                                                                       #           return

              #      elif args[0][0] != "@":

# #                       await self.highrise.send_whisper(user.id, f"Invalid user format. Please use '@username'.")                                                                               #                     return

    #                elif args[0][1:].lower() not in usernames:

     #                   await self.highrise.send_whisper(user.id, f"{args[0][1:]} is not in the room.")

      #                  return

       #             position_name = " ".join(args[1:])

        #            if position_name == 'vip':

         #               dest = Position(14, 10, 26)                                                      #          elif position_name == 'pool':

           #             dest = Position(1.5, 1, 7.5)

#                                                                                                #                   else:

  #                      try:

   #                         messages = position_name.split(',')

    #                        x=int(messages[0])                                                      #                       y=int(messages[1])

      #                      z=int(messages[2])

       #                     dest = Position(x,y,z)

        #                except:                                                                         #                   return await self.highrise.send_whisper(user.id, f"Unkown location ")

          #          if not user_id:

           #             await self.highrise.send_whisper(user.id, f"User {args[0][1:]} not found")

            #            return

             #       await self.highrise.teleport(user_id, dest)

              #      await self.highrise.send_whisper(user.id, f"Teleported {args[0][1:]} to ({dest.x}, {dest.y}, {dest.z})")

               ## else:

 #                   await self.highrise.send_whisper(user.id, "You can't use this command")

                                                                                                #            else:

#

 #              pass                                                                              #      except:

   #         await self.highrise.send_whisper(user.id,f"لقد خرج من الغرفة")
