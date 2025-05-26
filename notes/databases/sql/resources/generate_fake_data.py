import random
from datetime import date, timedelta

from faker import Faker

# Configuración de Faker
fake = Faker("es_ES")  # Usamos español para nombres y descripciones

# --- Configuración de la cantidad de registros a generar ---
NUM_PROVEEDORES = 50
NUM_CLIENTES = 200
NUM_PRODUCTOS = 1000
NUM_VENTAS = 5000
NUM_VENTAS_DETALLE_PER_VENTA = 3  # Promedio de ítems por venta

# --- Generación de IDs para mantener la referencia ---
proveedor_ids = []
cliente_ids = []
producto_ids = []
venta_ids = []

# --- Encabezado del archivo SQL ---
print("-- SQL generado para SQLite")
print("-- Habilitar la verificación de claves foráneas (importante para SQLite)")
print("PRAGMA foreign_keys = ON;")
print()

# --- INICIAR UNA TRANSACCIÓN GRANDE AQUÍ para una importación más rápida ---
print("BEGIN TRANSACTION;")
print()

# --- DROP TABLES (en orden inverso de dependencia para asegurar que no haya errores de FK) ---
print("-- 1. DROP TABLES")
print('DROP TABLE IF EXISTS "ventas_detalle";')
print('DROP TABLE IF EXISTS "ventas";')
print('DROP TABLE IF EXISTS "productos";')
print('DROP TABLE IF EXISTS "clientes";')
print('DROP TABLE IF EXISTS "proveedores";')
print()

# --- CREATE TABLES (en orden de dependencia) ---
print("-- 2. CREATE TABLES")
print("""
CREATE TABLE IF NOT EXISTS "proveedores" (
  "Prov_Id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "Prov_Nombre" TEXT NOT NULL DEFAULT '0'
);

CREATE TABLE IF NOT EXISTS "clientes" (
  "Cli_Id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "Cli_RazonSocial" TEXT NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS "productos" (
  "Prod_Id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "Prod_Descripcion" TEXT NOT NULL DEFAULT '',
  "Prod_Color" TEXT NOT NULL DEFAULT '',
  "Prod_Status" INTEGER NOT NULL DEFAULT '1',
  "Prod_Precio" REAL NOT NULL DEFAULT '0.00',
  "Prod_ProvId" INTEGER DEFAULT '0',
  FOREIGN KEY ("Prod_ProvId") REFERENCES "proveedores"("Prov_Id")
);

CREATE TABLE IF NOT EXISTS "ventas" (
  "Ventas_Id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "Ventas_Fecha" TEXT NOT NULL,
  "Ventas_CliId" INTEGER NOT NULL DEFAULT '0',
  "Ventas_NroFactura" INTEGER NOT NULL DEFAULT '0',
  "Ventas_Neto" REAL NOT NULL DEFAULT '0.00',
  "Ventas_Iva" REAL NOT NULL DEFAULT '0.00',
  "Ventas_Total" REAL NOT NULL DEFAULT '0.00',
  FOREIGN KEY ("Ventas_CliId") REFERENCES "clientes"("Cli_Id")
);

CREATE TABLE IF NOT EXISTS "ventas_detalle" (
  "VD_Id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "VD_VentasId" INTEGER NOT NULL DEFAULT '0',
  "VD_ProdId" INTEGER NOT NULL DEFAULT '0',
  "VD_Cantidad" INTEGER NOT NULL DEFAULT '0',
  "VD_Precio" REAL NOT NULL DEFAULT '0.00',
  "VD_Costo" REAL NOT NULL DEFAULT '0.00',
  FOREIGN KEY ("VD_VentasId") REFERENCES "ventas"("Ventas_Id"),
  FOREIGN KEY ("VD_ProdId") REFERENCES "productos"("Prod_Id")
);
""")
print()

# --- DELETE FROM (para limpiar tablas existentes antes de insertar nuevos datos) ---
print("-- 3. DELETE FROM")
print('DELETE FROM "ventas_detalle";')
print('DELETE FROM "ventas";')
print('DELETE FROM "productos";')
print('DELETE FROM "clientes";')
print('DELETE FROM "proveedores";')
print()

# --- 4. INSERT DATA (¡EN ESTE ORDEN PARA RESPETAR LAS CLAVES FORÁNEAS!) ---

print("-- 4.1. Insertando datos en 'proveedores'")
for i in range(1, NUM_PROVEEDORES + 1):
    proveedor_ids.append(i)
    nombre = fake.company().replace("'", "''")  # Escapar comillas simples
    print(
        f'INSERT INTO "proveedores" ("Prov_Id", "Prov_Nombre") VALUES ({i}, \'{nombre}\');'
    )
print()

print("-- 4.2. Insertando datos en 'clientes'")
for i in range(1, NUM_CLIENTES + 1):
    cliente_ids.append(i)
    razon_social = fake.company().replace("'", "''")
    print(
        f'INSERT INTO "clientes" ("Cli_Id", "Cli_RazonSocial") VALUES ({i}, \'{razon_social}\');'
    )
print()

print("-- 4.3. Insertando datos en 'productos'")
for i in range(1, NUM_PRODUCTOS + 1):
    producto_ids.append(i)
    descripcion = fake.catch_phrase().replace("'", "''")
    color = fake.color_name().replace("'", "''")
    status = random.choice([0, 1])
    precio = round(random.uniform(5.0, 500.0), 2)
    prov_id = random.choice(proveedor_ids)  # Selecciona un proveedor existente
    print(
        f'INSERT INTO "productos" ("Prod_Id", "Prod_Descripcion", "Prod_Color", "Prod_Status", "Prod_Precio", "Prod_ProvId") VALUES ({i}, \'{descripcion}\', \'{color}\', {status}, {precio:.2f}, {prov_id});'
    )
print()

print("-- 4.4. Insertando datos en 'ventas'")
start_date = date(2023, 1, 1)
end_date = date(2024, 12, 31)
time_delta = (end_date - start_date).days

for i in range(1, NUM_VENTAS + 1):
    venta_ids.append(i)
    fecha = start_date + timedelta(days=random.randint(0, time_delta))
    cli_id = random.choice(cliente_ids)  # Selecciona un cliente existente
    nro_factura = random.randint(1000, 9999)
    neto = round(random.uniform(10.0, 2000.0), 2)
    iva = round(neto * 0.21, 2)  # Asumiendo un 21% de IVA
    total = round(neto + iva, 2)
    print(
        f'INSERT INTO "ventas" ("Ventas_Id", "Ventas_Fecha", "Ventas_CliId", "Ventas_NroFactura", "Ventas_Neto", "Ventas_Iva", "Ventas_Total") VALUES ({i}, \'{fecha}\', {cli_id}, {nro_factura}, {neto:.2f}, {iva:.2f}, {total:.2f});'
    )
print()

print("-- 4.5. Insertando datos en 'ventas_detalle'")
# Para cada venta, generamos algunos detalles
detalle_id_counter = 1
for venta_id in venta_ids:
    num_items = random.randint(
        1, NUM_VENTAS_DETALLE_PER_VENTA * 2
    )  # Cantidad variable de ítems por venta
    for _ in range(num_items):
        prod_id = random.choice(producto_ids)  # Selecciona un producto existente
        cantidad = random.randint(1, 10)
        # Aquí, idealmente, buscaríamos el precio real del producto,
        # pero para datos falsos, podemos simularlo o simplemente usar un valor aleatorio
        precio_unitario = round(
            random.uniform(5.0, 500.0), 2
        )  # Precio del ítem en la venta
        costo_unitario = round(
            precio_unitario * random.uniform(0.5, 0.8), 2
        )  # Costo simulado
        print(
            f'INSERT INTO "ventas_detalle" ("VD_Id", "VD_VentasId", "VD_ProdId", "VD_Cantidad", "VD_Precio", "VD_Costo") VALUES ({detalle_id_counter}, {venta_id}, {prod_id}, {cantidad}, {precio_unitario:.2f}, {costo_unitario:.2f});'
        )
        detalle_id_counter += 1
print()

# --- FINALIZAR LA TRANSACCIÓN AQUÍ ---
print("COMMIT;")  # <--- AÑADIDA PARA UNA IMPORTACIÓN MÁS RÁPIDA
print()

print("-- Fin de la generación de datos.")
