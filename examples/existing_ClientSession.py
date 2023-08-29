import aiohttp

from aiosurrealdb import SurrealHTTP


async def main():
    # This session could be created elsewhere and passed in as an argument.
    async with aiohttp.ClientSession() as session:
        async with SurrealHTTP(
            url="http://localhost:8000",
            namespace="test",
            username="root",
            password="root",
            database="test",
            session=session,
        ) as db:
            await db.create(
                "person",
                {
                    "user": "me",
                    "pass": "safe",
                    "marketing": True,
                    "tags": ["python", "documentation"],
                },
            )

            # Here we select a person and do an update on the first returned ID.
            p = await db.select("person")
            pid = p[0]["id"]
            print(
                await db.update(
                    pid,
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
            # doing all of the above and more in SurrealQl

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
