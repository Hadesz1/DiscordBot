#! /usr/bin/env python3
#|*****************************************************
# * Copyright         : Copyright (C) 2019
# * Author            : ddc
# * License           : GPL v3
# * Python            : 3.6
#|*****************************************************
# # -*- coding: utf-8 -*-

from src.cogs.bot.utils import bot_utils as utils
from src.databases.sqlite3.connection import Sqlite3
from src.databases.postgres.connection import PostgreSQL
################################################################################
################################################################################
################################################################################ 
class Databases():
    def __init__(self, log):
        self.log = log
        self.database_in_use = utils.get_settings("Bot", "DatabaseInUse")
################################################################################
################################################################################
################################################################################
    async def check_database_connection(self):
        if self.database_in_use == "sqlite":
            sqlite3 = Sqlite3(self.log)
            return await sqlite3.create_connection()
        elif self.database_in_use == "postgres":
            postgreSQL = PostgreSQL(self.log)
            return await postgreSQL.create_connection()        
################################################################################
################################################################################
################################################################################
    async def execute(self, sql):
        if self.database_in_use == "sqlite":
            sqlite3 = Sqlite3(self.log)
            await sqlite3.executescript(sql)
        elif self.database_in_use == "postgres":
            postgreSQL = PostgreSQL(self.log)
            await postgreSQL.execute(sql)
################################################################################
################################################################################
################################################################################
    async def select(self, sql):
        if self.database_in_use == "sqlite":
            sqlite3 = Sqlite3(self.log)
            return await sqlite3.select(sql)
        elif self.database_in_use == "postgres":
            postgreSQL = PostgreSQL(self.log)
            return await postgreSQL.select(sql)
################################################################################
################################################################################
################################################################################
    async def set_primary_key_type(self):
        if self.database_in_use == "sqlite":
            return "INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE"
        elif self.database_in_use == "postgres":
            return "BIGSERIAL NOT NULL PRIMARY KEY UNIQUE"
################################################################################
################################################################################
################################################################################
