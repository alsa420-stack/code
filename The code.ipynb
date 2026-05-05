
# 1. Why Start With The "TASK" CLASS?
# I start with Task because it represents the "Input Data".The system cannot exist without knowing what the client needs first.
class Task:
    def __init__(self, client, service, user_num):
        self.client = client  # Information about the recipient
        self.service = service  # Information about the work type
        self.user_num = user_num  # Critical value for agents to process logic
        self.desc = f"{service} for {client}"

# 2. Why define "RECOMMENDATION" next? # This defines the "Format of the Output". We need to know how the results will look before the agents create them.
class Recommendation:# Stores agent outputs
    def __init__(self, agent_name, content):
        self.agent_name = agent_name
        self.content = content

    def __str__(self):
        return f"[{self.agent_name}] recommends: {self.content}"
# 3.Why "Memory" Third? To ensure "Data Continuity". We must have a storage place
class Memory:# Store decisions, apply Encapsulation and review history document work
    def __init__(self):
        self.history = []#List acting as a database for activities

    def log(self, recommendation):
        self.history.append(recommendation)

    def show(self):
        print(" ICON 01 MEMORY HISTORY ")
        for rec in self.history: print(rec)
# 4. Why "KNOWLEDGE BASE"? This is the "System Brain". It contains the fixed rules and constants. That agents need to reference to perform their calculations.
class KnowledgeBase:
    def __init__(self):
        # Encapsulating business constraints and global variables
        self.data = {"Top": 20000, "revenue": 7000, "exp": 4680, "color": "Brown & Grey"}

    def get(self, key):
        return self.data.get(key)
# 5. Why "Agents" after data components? Agents are the "Workers". They need the Task (Input),KnowledgeBase (Rules), and Recommendation (Format) to do their job
class Agent:
    def __init__(self, name,kb):
        self.name= name
        self.kb =kb

    def process(self, task):
        pass

class IconIdentityAgent(Agent):#Specialized for Branding
    def process(self, task):
        content = f"Apply {self.kb.get('color')} branding for {task.client}."
        return Recommendation(self.name, content)#Packaging the agent's name and its findings to be sent to the Founder

class GrowthAgent(Agent):#Specialized for Business growth and strategy
    def process(self, task):
        # Decisions based on Task data vs KnowledgeBase thresholds
        if task.user_num < self.kb.get('Top'):
            content = "Status: Emerging. Strategy: Keep it FREE to build trust."
        else:
            content = "Status: Established. Strategy: Transition to Premium."
        return Recommendation(self.name, content)

class FinanceAgent(Agent):# Specialized for Sustainability
    def process(self, task):
        profit = self.kb.get('revenue') - self.kb.get('exp')
        content = f"Financial Health: Stable. Estimated Profit: {profit}."
        return Recommendation(self.name, content)

# 6.Why "Founder" last? The Founder is the "Controller".The Controller must be defined last
# because it manages and orchestrates all the objects created above
class Founder:
    def __init__(self, name):
        self.name = name

    def run(self, agents, task, memory):
        print(f"WELCOME! , Founder {self.name} manages the system...")
        for agent in agents:
            rec = agent.process(task)# Activating agents (Polymorphism)
            print(f"Receiving: {rec}")
            memory.log(rec)  # Saving results immediately
        # Final step: Founder reviews all and decides
        self.make_decision()

    def make_decision(self):
# This ensures the decision appears in the output before the memory history
        print(f" Final Decision by {self.name}:")
        print(f"I have reviewed the Identity, Growth, and Finance reports. Strategy is approved")
        #System Execution
if __name__ == "__main__":
    kb= KnowledgeBase()# 1. Creating the 'KnowledgeBase' Object That acts as the system's brain, holding all shared rules.
    mem = Memory() # 2. Creating the 'Memory' Object .This object acts as a storage container to save all agent outputs.
    alaa = Founder("Alaa")# 3. Creating the 'Founder' Object .This object represents the decision-maker (Alaa) who controls the system
    my_agents = [#4.Creating Agent Objects I create three distinct objects, each specialized in a different business task:
        IconIdentityAgent("Identity-Agent", kb),#Identity Agent Object
        GrowthAgent("Growth-Agent", kb),#Growth Agent Object
        FinanceAgent("Finance-Agent", kb)#Finance Agent Object
    ]
    current_task = Task("Global Corp", "Full Branding", 15864) # 5.Creating the 'Task' Object.This object encapsulates the specific request details (Client name, Service, User count)

    alaa.run(my_agents, current_task, mem)
    print("-" *50)
    mem.show()
