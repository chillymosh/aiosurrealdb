# aiosurrealdb

aiosurrealdb is a fully asynchronous version of the SurrealDB driver that uses aiohttp.
  
The reason behind using aiohttp is that many modern async frameworks and libraries, especially for bots, such as those for Discord, already have aiohttp installed as a dependency. So it made more sense to utilise an already installed library and most likely an already exisitng ClientSession.

**Connection Methods**

- http
- websocket 

Installation
---------------------------
The following commands are currently the valid ways of installing aiosurrealdb.

**aiosurrealdb requires Python 3.10+**

**Windows**

.. code:: sh

    py -3.10 -m pip install -U aiosurrealdb

**Linux**

.. code:: sh

    python3.10 -m pip install -U aiosurrealdb

Getting Started
----------------------------
**See more** `Examples <https://github.com/chillymosh/aiosurrealdb/tree/dev/examples>`_

.. code:: py
  
  from aiosurrealdb import Surreal
  
  
  async def main():
      """Example of how to use the aiosurrealdb client."""
      async with Surreal("ws://localhost:8000/rpc") as db:
          await db.signin({"user": "root", "pass": "root"})
          await db.use("test", "test")
          await db.create(
              "person",
              {
                  "user": "me",
                  "pass": "safe",
                  "marketing": True,
                  "tags": ["python", "documentation"],
              },
          )
          print(await db.select("person"))
          print(
              await db.update(
                  "person",
                  {
                      "user": "you",
                      "pass": "very_safe",
                      "marketing": False,
                      "tags": ["Awesome"],
                  },
              )
          )
          print(await db.delete("person"))
  
          # You can also use the query method
          # doing all of the above and more in SurrealQL
  
          # In SurrealQL you can do a direct insert
          # and the table will be created if it doesn't exist
          await db.query(
              """
          insert into person {
              user: 'me',
              pass: 'very_safe',
              tags: ['python', 'documentation']
          };
          
          """
          )
          print(await db.query("select * from person"))
  
          print(
              await db.query(
                  """
          update person content {
              user: 'you',
              pass: 'more_safe',
              tags: ['awesome']
          };
          
          """
              )
          )
          print(await db.query("delete person"))
  
  
  if __name__ == "__main__":
      import asyncio
  
      asyncio.run(main())
