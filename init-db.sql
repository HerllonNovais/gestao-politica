CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Tabela de usuários
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    nome VARCHAR(100) NOT NULL,
    ativo BOOLEAN DEFAULT TRUE,
    criado_em TIMESTAMP DEFAULT NOW()
);

-- Tabela de eleitores
CREATE TABLE eleitores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    email VARCHAR(255),
    endereco TEXT,
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    criado_em TIMESTAMP DEFAULT NOW()
);

-- Tabela de campanhas
CREATE TABLE campanhas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    mensagem TEXT NOT NULL,
    data_disparo TIMESTAMP NOT NULL,
    status VARCHAR(20) DEFAULT 'agendada',
    criado_em TIMESTAMP DEFAULT NOW()
);
