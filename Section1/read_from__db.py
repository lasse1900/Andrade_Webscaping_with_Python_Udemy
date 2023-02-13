import sqlite3

# Connect to database
conn = sqlite3.connect('output/all_jobs.db')

# Create a cursor
c = conn.cursor()

# Query the database
c.execute("SELECT title FROM jobs")
#print(c.fetchone())
print(c.fetchall())

# Commit the command
conn.commit()

# Close connection
conn.close()