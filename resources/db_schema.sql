CREATE TABLE "types" ( `id` INTEGER NOT NULL, `name` TEXT NOT NULL UNIQUE, PRIMARY KEY(`id`) )

CREATE TABLE "files" ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `path` TEXT NOT NULL UNIQUE, `type` INTEGER, FOREIGN KEY(`type`) REFERENCES `types`(`id`) )

CREATE TABLE `cat_experiencial` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `name` TEXT NOT NULL UNIQUE )
CREATE TABLE `cat_geografico` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `provincia` TEXT NOT NULL, `municipio` TEXT, `zona_turistica` TEXT )
CREATE TABLE `cat_temporal` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `name` TEXT NOT NULL UNIQUE )
CREATE TABLE `cat_vivencial` ( `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, `name` TEXT NOT NULL UNIQUE )

CREATE TABLE `classifications` ( `id` INTEGER NOT NULL, `file` INTEGER NOT NULL UNIQUE, `cat_geo` INTEGER, `cat_exp` INTEGER, `cat_viv` INTEGER, `cat_temp` INTEGER, FOREIGN KEY(`cat_exp`) REFERENCES `cat_experiencial`(`id`), FOREIGN KEY(`cat_viv`) REFERENCES `cat_vivencial`(`id`), FOREIGN KEY(`cat_temp`) REFERENCES `cat_temporal`(`id`) )
