import pandas as pd

states = ["California", "Florida", "Michigan", "Ohio"]
population = [39613455, 29744211, 21944577, 19299981]


dict_states = {'States':states, 'Population': population}

df_states = pd.DataFrame.from_dict(dict_states)
# print(df_states)
df_states.to_csv('states.csv', index=False)



# for state in states:
#     print(state)


# with open('test.txt', 'w') as file:
#     file.write("Data written succesfully!")

