import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_new_user(self, tg_id, username, f_name, l_name, email, b_year):
        self.cursor.execute(f"INSERT INTO users (tg_username, tg_firstname, tg_lastname, tg_id, email, birth_year)"
                            f"VALUES (?, ?, ?, ?);", (username, f_name, l_name, tg_id, email, b_year))
        self.conn.commit()

    def update_user(self, tg_id, full_name, phone):
        self.cursor.execute(f"UPDATE users  SET full_name=?, tg_phone"
                            f"WHERE tg_id=?;", (full_name, phone, tg_id))
        self.conn.commit()

    def get_user(self, tg_id):
        users = self.cursor.execute(f"SELECT * FROM users WHERE tg_id=?;", (tg_id,))
        return users.fetchone()

    def get_user_by_username(self, user_name):
        users = self.cursor.execute(f"SELECT * FROM users WHERE tg_username=?;", (user_name,))
        return users.fetchone()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    # Work with categories
    def get_categories(self):
        categories = self.cursor.execute("SELECT id, category_name FROM categories;")
        return categories

    def add_category(self, new_cat):
        categories = self.cursor.execute(
            "SELECT id, category_name FROM categories WHERE category_name=?;",
            (new_cat,)
        ).fetchone()
        print(categories)
        if not categories:
            try:
                self.cursor.execute(
                    "INSERT INTO categories (category_name) VALUES(?);",
                    (new_cat,)
                )
                self.conn.commit()
                res = {
                    'status': True,
                    'desc': 'Successfully added'
                }
                return res
            except Exception as e:
                res = {
                    'status': False,
                    'desc': 'Something error, please, try again'
                }
                return res
        else:
            res = {
                'status': False,
                'desc': 'exists'
            }
            return res

    def upd_category(self, new_cat, old_cat):
        categories = self.cursor.execute(
            "SELECT id, category_name FROM categories WHERE category_name=?;",
            (new_cat,)
        ).fetchone()

        if not categories:
            try:
                self.cursor.execute(
                    "UPDATE categories SET category_name=? WHERE category_name=?;",
                    (new_cat, old_cat)
                )
                self.conn.commit()
                res = {
                    'status': True,
                    'desc': 'Successfully updated'
                }
                return res
            except Exception as e:
                res = {
                    'status': False,
                    'desc': 'Something error, please, try again'
                }
                return res
        else:
            res = {
                'status': False,
                'desc': 'exists'
            }
            return res

    def edit_category(self, new_name, id):
        try:
            self.cursor.execute(
                "UPDATE categories SET category_name=? WHERE id=?",
                (new_name, id)
            )
            self.conn.commit()
            return True
        except:
            return False

    def del_category(self, cat_name):
        try:
            self.cursor.execute("DELETE FROM categories WHERE category_name=?", (cat_name,))
            self.conn.commit()
            return True
        except:
            return False

    def get_products(self, cat_id):
        products = self.cursor.execute(
            f"SELECT id, product_name, product_image FROM products WHERE product_category=?;",
            (cat_id,))
        return products

    def add_product(self, new_cat):
        products = self.cursor.execute(
            "SELECT id, product_name FROM products WHERE product_name=?;",
            (new_cat,)
        ).fetchone()
        print(products)
        if not products:
            try:
                self.cursor.execute(
                    "INSERT INTO products (product_name) VALUES(?);",
                    (new_cat,)
                )
                self.conn.commit()
                res = {
                    'status': True,
                    'desc': 'Successfully added'
                }
                return res
            except Exception as e:
                res = {
                    'status': False,
                    'desc': 'Something error, please, try again'
                }
                return res
        else:
            res = {
                'status': False,
                'desc': 'exists'
            }
            return res

    def upd_product(self, new_cat, old_cat):
        products = self.cursor.execute(
            "SELECT id, product_name FROM products WHERE product_name=?;",
            (new_cat,)
        ).fetchone()

        if not products:
            try:
                self.cursor.execute(
                    "UPDATE products SET product_name=? WHERE product_name=?;",
                    (new_cat, old_cat)
                )
                self.conn.commit()
                res = {
                    'status': True,
                    'desc': 'Successfully updated'
                }
                return res
            except Exception as e:
                res = {
                    'status': False,
                    'desc': 'Something error, please, try again'
                }
                return res
        else:
            res = {
                'status': False,
                'desc': 'exists'
            }
            return res

    def edit_product(self, new_name, id):
        try:
            self.cursor.execute(
                "UPDATE products SET product_name=? WHERE id=?",
                (new_name, id)
            )
            self.conn.commit()
            return True
        except:
            return False

    def del_product(self, name, id):
        try:
            self.cursor.execute(
                "DELETE FROM products WHERE id=?, product_name=?",
                (name, id)
            )
            self.conn.commit()
            return True
        except:
            return False
    def insert_ad(self, title, text, price, image, phone, u_id, prod_id, date):
        try:
            self.cursor.execute(
                f"INSERT INTO ads (ad_title, ad_text, ad_price, ad_images, ad_phone, ad_owner, ad_product, ad_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (title, text, price, image, phone, u_id, prod_id, date)
            )
            self.conn.commit()
            return True
        except:
            return False

    def get_my_ads(self, u_id):
        ads = self.cursor.execute(
            f"SELECT id, ad_title, ad_text, ad_price, ad_images FROM ads WHERE ad_owner=?;",
            (u_id,)
        )
        return ads

    def get_search_ads(self, u_id, search_term):
        ads = self.cursor.execute(
            f"SELECT id, ad_title, ad_text, ad_price, ad_images FROM ads WHERE ad_text ILIKE %s;",
            (f"%{search_term}%",))
        return ads.fetchall()

