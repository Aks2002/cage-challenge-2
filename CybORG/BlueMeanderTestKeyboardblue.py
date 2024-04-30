from CybORG import CybORG
import inspect
import json
from CybORG.Agents.SimpleAgents.BlueMeanderKeyboardAgent import*
from CybORG.Agents.SimpleAgents.GreenAgent import GreenAgent
from CybORG.Agents.Wrappers.BlueTableWrapper import BlueTableWrapper
from CybORG.Agents import B_lineAgent
from CybORG.Agents.SimpleAgents.Meander import RedMeanderAgent

if __name__ == "__main__":
    print("Setup")
    path = str(inspect.getfile(CybORG))
    path = path[:-10] + '/Shared/Scenarios/Scenario2.yaml'

    agents = {'Red': RedMeanderAgent,'Green': GreenAgent}

    cyborg = BlueTableWrapper(CybORG(path, 'sim',agents=agents), output_mode='table')

    agent_name = 'Blue'

    results = cyborg.reset(agent=agent_name)
    observation = results.observation
    print(type(observation))
    action_space = results.action_space

    agent = KeyboardAgent()

    reward = 0
    for step in range(10):
        action = agent.get_action(observation, action_space)
        results = cyborg.step(agent=agent_name, action=action)
        print(cyborg.get_last_action(agent='Red'))
        print('>>> Reward: ', results.reward)
        reward += results.reward
        observation = results.observation

        table_data = [row for row in observation._rows]
        json_data = []
        for row in table_data:
            json_row = {}
            for idx, column in enumerate(observation.field_names):
                json_row[column] = row[idx]
            json_data.append(json_row)
        json_string = json.dumps(json_data, indent=4)
        print(json_string)





    print(f"Game Over. Total reward: {reward}")
