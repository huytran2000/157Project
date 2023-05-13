
/* drop table movie; drop table tv_show; drop table product_trailer;
drop table product_participant; drop table product_genre; drop table product_characteristic; drop table product_year;
drop table product_episode; drop table product; drop table profile_product; drop table subscriber_profile; */
create table product (product_id int not null primary key,
                      title varchar not null,
                      debut_year int not null,
                      parental_rating varchar null,
                      description varchar not null,
                      netflix_release_year int not null,
                      language varchar not null,
                      check (debut_year >= 0 and netflix_release_year >= 1997 and netflix_release_year >= debut_year));
create table movie (product_id int not null primary key references product(product_id) on delete cascade on update cascade,
                    movie_length text not null,
                    check (movie_length >= '00:00:00'));
create table tv_show (product_id int not null primary key references product(product_id) on delete cascade on update cascade);
create table trailer (trailer_id int not null primary key,
                      product_id int not null references product(product_id) on delete cascade on update cascade,                
                      title varchar not null,
                      length text not null,
                      check (length > '00:00:00') );
create table product_participant (product_id int not null references product(product_id) on delete cascade on update cascade,
                                  participant_id int not null,
                                  name varchar not null,
                                  role varchar not null,
                                  primary key (product_id, participant_id),
                                  check (role == 'actor' or role == 'creator' or role == 'both'));
create table product_genre (product_id int not null references product(product_id) on delete cascade on update cascade,
                            genre varchar not null,
                            primary key (product_id, genre));
create table product_characteristic (product_id int not null references product(product_id) on delete cascade on update cascade,
                                     characteristic varchar not null,
                                     primary key (product_id, characteristic));
create table product_year (product_id int not null references product(product_id) on delete cascade on update cascade,
                           year int not null,
                           yearly_view_count int not null,
                           primary key (product_id, year),
                           check (year >= 1997 and yearly_view_count >= 0));
create table episode (episode_id int not null primary key,
                      product_id int not null references product(product_id) on delete cascade on update cascade,
                      title varchar not null,
                      description varchar not null,
                      length text not null,
                      debut_year int not null,
                      check (debut_year >= 0 and length >= '00:00:00'));
create table subscriber (subscriber_id int not null primary key,
                         phone_number varchar(10) null unique,
                         email_address varchar null unique,
                         password varchar not null,
                         dob text null,
                         payment_plan varchar not null,
                         max_resolution varchar not null,
                         advertisement int not null,
                         max_screens int not null,
                         check (length(phone_number) == 10 and length(password) >= 6 and length(password) <= 60 
                                and dob >= '1900-01-01' and (advertisement == 0 or advertisement == 1) and max_screens > 0));
create table profile_product (profile_id int not null,
                              product_id int not null references product(product_id) on update cascade,
                              subscriber_id int not null references subscriber(subscriber_id),
                              profile_name varchar not null,
                              product_status varchar not null,
                              primary key (profile_id, product_id),
                              check (product_status == 'liked' or product_status == 'listed' or product_status == 'both'));

/* turn on referential constraint */
PRAGMA foreign_keys = on;

        