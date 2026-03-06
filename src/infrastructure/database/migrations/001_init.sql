create table if not exists users(
    id serial primary key,
    tg_id integer not null,
    name text not null,
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp
);

create table if not exists meals(
    id serial primary key,
    user_id: integer not null,
    food_name text not null,
    created_at timestamp default current_timestamp,
    updated_at timestamp default current_timestamp,

    FOREIGN KEY (user_id) REFERENCES users(id)
);