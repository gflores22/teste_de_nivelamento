CREATE TABLE operadoras (
    Registro_ANS INT PRIMARY KEY,
    CNPJ VARCHAR(14) NOT NULL UNIQUE,
    Razao_Social VARCHAR(255) NOT NULL,
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(50) NOT NULL,
    Logradouro VARCHAR(255) NOT NULL,
    Numero VARCHAR(10) NOT NULL,
    Complemento VARCHAR(255),
    Bairro VARCHAR(100) NOT NULL,
    Cidade VARCHAR(100) NOT NULL,
    UF VARCHAR(2) NOT NULL,
    CEP VARCHAR(10) NOT NULL,
    DDD VARCHAR(3),
    Telefone VARCHAR(15) NOT NULL,
    Fax VARCHAR(15),
    Endereco_eletronico VARCHAR(255) NOT NULL,
    Representante VARCHAR(255) NOT NULL,
    Cargo_Representante VARCHAR(100) NOT NULL,
    Regiao_de_Comercializacao INT,
    Data_Registro_ANS DATE NOT NULL
);

CREATE TABLE despesas(
    DATA DATE NOT NULL,
    REG_ANS INT NOT NULL PRIMARY KEY,
    CD_CONTA_CONTABIL INT NOT NULL,
    DESCRICAO VARCHAR(255),
    VL_SALDO_INICIAL DECIMAL(15, 2),
    VL_SALDO_FINAL DECIMAL(15, 2),
    FOREIGN KEY (REG_ANS) REFERENCES operadoras(Registro_ANS)
);

-- Importação de dados para a tabela operadoras
-- substitua o caminho do arquivo CSV pelo caminho correto no seu sistema
LOAD DATA LOCAL INFILE 'C:/Users/gabri/OneDrive/Desktop/Gabriel/Testes/Banco de Dados/csv/Relatorio_cadop.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, Representante, Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS);

-- Importação de dados para a tabela despesas
LOAD DATA LOCAL INFILE './csv/1T2023.csv'
INTO TABLE despesas
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL);

LOAD DATA LOCAL INFILE './csv/2T2023.csv'
INTO TABLE despesas
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL);

LOAD DATA LOCAL INFILE './csv/3T2023.csv'
INTO TABLE despesas
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL);

LOAD DATA LOCAL INFILE './csv/4T2023.csv'
INTO TABLE despesas
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL);

LOAD DATA LOCAL INFILE './csv/1T2024.csv'
INTO TABLE despesas
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL);

LOAD DATA LOCAL INFILE './csv/2T2024.csv'
INTO TABLE despesas
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL);

LOAD DATA LOCAL INFILE './csv/3T2024.csv'
INTO TABLE despesas
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL);

LOAD DATA LOCAL INFILE './csv/4T2024.csv'
INTO TABLE despesas
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL);

-- 10 operadoras com maiores despesas no ultimo trimestre
SELECT 
    o.Razao_Social AS Operadora,
    SUM(d.VL_SALDO_FINAL) AS Total_Despesas
FROM 
    despesas d
JOIN 
    operadoras o ON d.REG_ANS = o.Registro_ANS
WHERE 
    d.DESCRICAO LIKE "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR"
    AND d.DATA >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH)
GROUP BY 
    o.Razao_Social
ORDER BY 
    Total_Despesas DESC
LIMIT 10;

-- 10 operadoras com maiores despesas no ultimo ano
SELECT 
    o.Razao_Social AS Operadora,
    SUM(d.VL_SALDO_FINAL) AS Total_Despesas
FROM 
    despesas d
JOIN 
    operadoras o ON d.REG_ANS = o.Registro_ANS
WHERE 
    d.DATA >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY 
    o.Razao_Social
ORDER BY 
    Total_Despesas DESC
LIMIT 10;