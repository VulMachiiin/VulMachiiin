CREATE TABLE products (id INTEGER, 
                       name TEXT NOT NULL DEFAULT "placeholder", 
                       amount_in_stock INTEGER NOT NULL DEFAULT 0, 
                       cartridge_type INTEGER NOT NULL DEFAULT 1, 
                       amount_per_cartridge INTEGER NOT NULL DEFAULT 0,
                       PRIMARY KEY (id));

CREATE TABLE shelves (id INTEGER,
                      size_horizontal INTEGER NOT NULL DEFAULT 1,
                      size_vertical INTEGER NOT NULL DEFAULT 3,
                      PRIMARY KEY (id));

CREATE TABLE productsinshelve (product_id INTEGER,
                               shelf_id INTEGER,
                               x_coordinate INTEGER NOT NULL,
                               y_coordinate INTEGER NOT NULL,
                               amount_in_cartridge INTEGER NOT NULL,
                               PRIMARY KEY (product_id, shelf_id),
                               FOREIGN KEY (product_id) REFERENCES products (id)
                               ON DELETE CASCADE ON UPDATE NO ACTION,
                               FOREIGN KEY (shelf_id) REFERENCES shelves (id)
                               ON DELETE CASCADE ON UPDATE NO ACTION);
  
CREATE TABLE nodes (id INTEGER,
                    shelve_id INTEGER,
                    PRIMARY KEY(id)
                    FOREIGN KEY (shelv,e_id) REFERENCES shelves (id));

CREATE TABLE edges (edge_id INTEGER PRIMARY KEY,
                    node_one_id INTEGER,
                    node_two_id INTEGER,
                    weight INTEGER NOT NULL,
                    FOREIGN KEY (node_one_id) REFERENCES paths (id)
                    ON DELETE CASCADE ON UPDATE NO ACTION,
                    FOREIGN KEY (node_two_id) REFERENCES paths (id)
                    ON DELETE CASCADE ON UPDATE NO ACTION,
                    CONTSTRAINT unique_nodes UNIQUE (node_one_id, node_two_id));

CREATE TABLE edgeconnections (edge_connection_id INTEGER PRIMARY KEY,
                              direction INTEGER NOT NULL,
                              edge_two_id INTEGER,
                              FOREIGN KEY (edge_one_id) REFERENCES edges (edge_id)
                              ON DELETE CASCADE ON UPDATE NO ACTION,
                              FOREIGN KEY (edge_two_id) REFERENCES edges (edge_id)
                              ON DELETE CASCADE ON UPDATE NO ACTION,
                              CONTSTRAINT unique_edges UNIQUE (edge_one_id, edge_two_id));