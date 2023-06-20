import random
import webbrowser
import wikipedia

def TaskExecution(query):
    try:
        if "hello" in query or "hi" in query or "hey" in query:
            ans = "Hi", "Hello", "Hello, How are you", "Hello Dear, how can i help you.", "Hello Dear",\
                  "Hey i was really waiting for your presence", "Hello, Nice to meet you",\
                  "Hello Dear, How Are You"
            rd = random.choice(ans)
            return rd

        elif "how are you" in query or "are you fine" in query:
            ans = "I am fine", "I am fine, how are you dear", "Fine, dear!"
            rd = random.choice(ans)
            return rd

        elif "i am fine" in query:
            ans = "Mmmm..."
            return ans

        elif "what are you doing" in query:
            ans = "I am talking to you dear."
            return ans

        elif "are you single" in query:
            ans = "No i'm relationship with the internet or wifi."
            return ans

        elif "see you later" in query or "goodbye" in query or "bye" in query or "good night" in query\
                or "sleep" in query or "stop" in query or "not now" in query or"break" in query:
            ans = "Good Bye!", "Bye Bye!", "See You Later", "Thanks for using me, have a good day...", \
                  "See You", "See you again..."
            rd = random.choice(ans)
            return rd

# ................................................................................................................#
# ................................................................................................................#
# .............................................About..............................................................#

        elif "tell me your name" in query or "what is your name" in query or "your name" in query:
            ans = "My Name is Friday"
            return ans

        elif "tell me about your self" in query or "tell me about you" in query or "who are you" in query \
                or "what are you" in query:
            ans = "I am a chatbot, I am the sixth Version Of Era."
            return ans

        elif "who invent you" in query or "who made you" in query or "who make you" in query or \
                "who invented you" in query or "tell you the name of the inventor" in query or \
                "tell me the name of the one who made you" in query:
            ans = "I was made by Neeraj in March 2023."
            return ans

        elif "distance between indore to dewas" in query or "distance between dewas to indore" in query:
            ans = "The Distance is 39.9 kilometer and approx one hour reach with the N.H. 52 Road."
            return ans

# ................................................................................................................#
# ................................................................................................................#
# ..............................................Physics...........................................................#

        elif "tell me newton first law of motion" in query or "first law of motion" in query or \
                "newton first law of motion" in query or "newton first law" in query:
            ans = "Newton first law states that, a body at rest or uniform motion will continue " \
                  "to be at rest or uniform motion until and unless a net external force acts on it."
            return ans

        elif "tell me newton second law of motion"in query or "second law of motion" in query or \
                "newton second law of motion" in query or "newton second law" in query:
            ans = "The second law of motion states that, the force acting on the body is equal " \
                  "to the product of its mass and acceleration."
            return ans

        elif "tell me newton third law of motion" in query or "third law of motion" in query or \
                "newton third law of motion" in query or "newton third law" in query:
            ans = "Newton third law states that, there is an equal and opposite reaction for every action"
            rd = random.choice(ans)
            return rd

        elif "law of conservation of energy" in query or "conservation of energy" in query or \
                "conservation of energy law" in query or "law of conservation" in query:
            ans = "The law of conservation of energy states that, energy can neither be created nor destroyed."
            return ans

        elif "definition of scalar quantity" in query or "tell me the definition of scalar quantity" in query or \
                "definition of scalar quantity"in query or "scalar quantity" in query:
            ans = "A scalar quantity is defined as the physical quantity with only magnitude and no direction." \
                  " Examples are Mass, Speed, Distance, Time, Volume, Density and Temperature."
            return ans

        elif "definition of vector quantity" in query or "tell me the definition of vector quantity" in query or \
                "definition of vector quantity" in query or "vector quantity" in query:
            ans = "A vector quantity is defined as the physical quantity that has both directions " \
                  "as well as magnitude. Examples are Linear momentum, Acceleration, Displacement," \
                  " Momentum, Angular Velocity, Force, Electric field and Polarization"
            return ans

        elif "definition of mass" in query or "mass definition" in query or "mass" in query:
            ans = "The amount of matter present in any object or body is called mass. " \
                  "Represented by M.And Mass is equal to, volume into density." \
                  " And the S.I. unit of mass is  kilogram."
            return ans

        elif "definition of weight" in query or "weight definition" in query or "weight" in query or \
                "definition of wait" in query or "wait definition" in query or "wait" in query:
            ans = "Weight is defined as the amount of force acting on the mass of an object because of" \
                  " acceleration due to gravity. Represented by W. And Weight is equal to, mass into acceleration" \
                  " due to gravity. The S.I. unit of weight is Newton."
            return ans

        elif "speed" in query or "define speed" in query:
            ans = "Speed is the rate of change of distance. It is Scalar Quantity." \
                  " Speed equals to distance upon time. Speed is measured in meter per second"
            return ans

        elif "velocity" in query or "define velocity" in query:
            ans = "Velocity is the rate of change of displacement. It is Vector Quantity." \
                  " Velocity equals to displacement upon time. Velocity is measured in meter per second"
            return ans

        elif "define distance" in query:
            ans = "The complete length of the path between any two points is called distance." \
                  " Distance is a scalar quantity as it only depends upon the magnitude and not the direction. " \
                  "Distance equals to speed into time. S.l. unit of distance is meter."
            return ans

        elif "define displacement" in query:
            ans = "Displacement is the direct length between any two points when measured along the " \
                  "minimum path between them. Displacement is a vector quantity as it depends upon both " \
                  "magnitude and direction. Displacement equals to velocity into time. " \
                  "S.I. unit of displacement is meter."
            return ans

        elif "define time" in query:
            ans = "The measured or measurable period during which an action, process, or condition exists." \
                  " AND its S.I. unit is second."
            return ans

        elif "define volume" in query:
            ans = "A volume is simply defined as the amount of space occupied by any three-dimensional solid. " \
                  "These solids can be a cube, a cuboid, a cone, a cylinder or a sphere." \
                  " Volume of a solid is measured in cubic units."
            return ans

        elif "define density" in query:
            ans = "Density, volumetric mass density or specific mass is defined as the, " \
                  "substances mass per unit of volume. The symbol most often used for density is rho." \
                  " Density equals to mass per unit volume. Though the S.I. unit of density is " \
                  "kilogram per meter cube. And its reciprocal is specific volume."
            return ans

        elif "define temperature" in query:
            ans = "Temperature is the measure of hotness or coldness of a body measured using Celsius, Kelvin," \
                  " and Fahrenheit scales.The change in temperature is based on the amount of heat released " \
                  "or absorbed. The S.I. unit of temperature is Kelvin."
            return ans

        elif "define linear momentum" in query:
            ans = "Linear momentum is the vector quantity and defined as the product of the mass of an " \
                  "object, m, and its velocity, v. The units of linear momentum are kilogram meter per second."
            return ans

        elif "define acceleration" in query:
            ans = "The rate of change of velocity with respect to time. " \
                  "The S.I. unit of acceleration is meter per second square."
            return ans

        elif "define momentum" in query:
            ans = "The ability to keep increasing or developing the force that makes something move faster and" \
                  " faster. Momentum equals to mass into velocity. S.I. Unit is Kilogram meter per second."
            return ans

        elif "angular velocity" in query:
            ans = "Angular velocity is the vector measure of the rotation rate, which refers to how fast an" \
                  " object rotates or revolves relative to another point. Angular velocity is represented by" \
                  " the Greek letter omega (w, sometimes Q). It is measured in angle per unit time; hence," \
                  " the S.I. unit of angular velocity is radians per second."
            return ans

        elif "define force" in query:
            ans = "Push or pull of an object is considered a force. And the push or pull on an object " \
                  "with mass causes it to change its velocity.Force is an external agent capable of changing" \
                  " a body's state of rest or motion. It has a magnitude and a direction. The direction" \
                  " towards which the force is applied is known as the direction of the force." \
                  " The S.I. unit of force is Newton."
            return ans

        elif "define electric field" in query:
            ans = "A region around a charged particle or object within which a force would be exerted on other" \
                  " charged particles or objects. An electric field is also described as the electric force per" \
                  " unit charge. E equals to F by Q , where, E is the electric field. F is a force." \
                  " And Q is the charge."
            return ans

        elif 'what is' in query:
            import wikipedia as googleScrap
            query = query.replace('search', ' ')
            query = query.replace('What is ', ' ')
            try:
                result = googleScrap.summary(query, 1)
                return result
            except:
                return query


        else:
            webbrowser.open(query)
            return query

    except Exception as e:
        print(e, ", - I did not understand...")

# TaskExe()

'''            
            elif "" in query:
                ans = ""
                rd = random.choice(ans)
                print(rd)
'''