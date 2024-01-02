-- Find all products that were not sold  
-- Connect tables with JOIN invoice_item ON product.id = invoice_item.product_id

-- product
-- #id |  sku | product_name | price 
-- # 1 | 13 | Game of thrones      | 55
-- # 2|  23 | Capture Youth      | 66
-- # 3|  335 | Dewy Skin      | 88

-- invoice
-- # product_id 
-- #  1 | Alex       
-- #  7 | Riley    
-- # 5 | Tyler      

# if product id is not in invoice table, it was not sold

SELECT product.id, product.product_name
FROM product
LEFT JOIN invoice_item ON product.id = invoice_item.product_id
WHERE invoice_item.product_id IS NULL;