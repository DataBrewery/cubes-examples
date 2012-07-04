--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

--
-- Name: vvo; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA vvo;


ALTER SCHEMA vvo OWNER TO postgres;

SET search_path = vvo, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: dm_cpv; Type: TABLE; Schema: vvo; Owner: stefan; Tablespace: 
--

CREATE TABLE dm_cpv (
    id integer,
    code text,
    code_src text,
    code_wcheck text,
    level integer,
    division text,
    "group" text,
    class text,
    category text,
    detail text,
    division_compet numeric,
    group_compet numeric,
    class_compet numeric,
    category_compet numeric,
    detail_compet numeric,
    division_label_en text,
    group_label_en text,
    class_label_en text,
    category_label_en text,
    detail_label_en text,
    division_label_sk text,
    group_label_sk text,
    class_label_sk text,
    category_label_sk text,
    detail_label_sk text
);


ALTER TABLE vvo.dm_cpv OWNER TO stefan;

--
-- Name: dm_criteria; Type: TABLE; Schema: vvo; Owner: stefan; Tablespace: 
--

CREATE TABLE dm_criteria (
    id integer,
    code character varying,
    description_sk character varying,
    sdesc_sk character varying,
    description_en character varying,
    sdesc_en character varying
);


ALTER TABLE vvo.dm_criteria OWNER TO stefan;

--
-- Name: dm_date; Type: TABLE; Schema: vvo; Owner: stefan; Tablespace: 
--

CREATE TABLE dm_date (
    id integer,
    year integer,
    month integer,
    month_name_sk character varying,
    month_sname_sk character varying,
    month_name_en character varying,
    month_sname_en character varying,
    day integer,
    week_day integer,
    week_day_name_sk character varying,
    week_day_sname_sk character varying,
    week_day_name_en character varying,
    week_day_sname_en character varying
);


ALTER TABLE vvo.dm_date OWNER TO stefan;

--
-- Name: dm_geography; Type: TABLE; Schema: vvo; Owner: stefan; Tablespace: 
--

CREATE TABLE dm_geography (
    id integer,
    okres character varying,
    okres_code character varying,
    okres_regis character varying,
    kraj character varying,
    kraj_code character varying
);


ALTER TABLE vvo.dm_geography OWNER TO stefan;

--
-- Name: dm_process_type; Type: TABLE; Schema: vvo; Owner: stefan; Tablespace: 
--

CREATE TABLE dm_process_type (
    id integer,
    code character varying,
    description_sk character varying,
    sdesc_sk character varying,
    description_en character varying,
    sdesc_en character varying
);


ALTER TABLE vvo.dm_process_type OWNER TO stefan;

--
-- Name: dm_procurer; Type: TABLE; Schema: vvo; Owner: stefan; Tablespace: 
--

CREATE TABLE dm_procurer (
    id integer,
    ico character varying,
    name character varying,
    address text,
    region character varying,
    country character varying,
    date_start date,
    date_end date,
    legal_form character varying,
    legal_form_code integer,
    account_sector character varying,
    account_sector_code integer,
    ownership character varying,
    ownership_code integer,
    source character varying,
    date_created date,
    offer_count_avg numeric,
    competitiveness numeric
);


ALTER TABLE vvo.dm_procurer OWNER TO stefan;

--
-- Name: dm_supplier; Type: TABLE; Schema: vvo; Owner: stefan; Tablespace: 
--

CREATE TABLE dm_supplier (
    id integer,
    ico character varying,
    name character varying,
    address text,
    region character varying,
    country character varying,
    date_start date,
    date_end date,
    legal_form character varying,
    legal_form_code integer,
    account_sector character varying,
    account_sector_code integer,
    ownership character varying,
    ownership_code integer,
    source character varying,
    date_created date,
    offer_count_avg numeric,
    competitiveness numeric
);


ALTER TABLE vvo.dm_supplier OWNER TO stefan;

--
-- Name: ft_contracts; Type: TABLE; Schema: vvo; Owner: stefan; Tablespace: 
--

CREATE TABLE ft_contracts (
    id integer,
    document_id integer,
    document_code character varying,
    contract_key character varying,
    document_type_code character varying,
    vz_flag integer,
    bulletin_number character varying,
    announcement_number character varying,
    source_url character varying,
    bulletin_date_id integer,
    bulletin_date date,
    contract_name text,
    process_type_id integer,
    contract_type_id integer,
    criteria_id integer,
    elektronicka_aukcia_flag integer,
    zakazka_eurofondy_flag integer,
    cpv_id integer,
    cpv_code character varying,
    procurer_id integer,
    supplier_id integer,
    geography_id integer,
    predpoklad_subdodavok character varying,
    pocet_ponuk integer,
    pocet_zmluv integer,
    procurement_amount numeric,
    procurement_currency character varying,
    contract_amount numeric,
    contract_currency character varying
);


ALTER TABLE vvo.ft_contracts OWNER TO stefan;

--
-- Name: dm_account_sector; Type: TABLE; Schema: vvo; Owner: stefan; Tablespace: 
--

CREATE TABLE dm_account_sector (
    id integer,
    sektor character varying,
    sektor_code integer,
    sektor_desc character varying,
    sektor_sdesc character varying
);


ALTER TABLE vvo.dm_account_sector OWNER TO stefan;

--
-- Name: dm_contract_type; Type: TABLE; Schema: vvo; Owner: stefan; Tablespace: 
--

CREATE TABLE dm_contract_type (
    id integer,
    code character varying,
    description character varying,
    sdesc character varying
);


ALTER TABLE vvo.dm_contract_type OWNER TO stefan;

--
-- PostgreSQL database dump complete
--

