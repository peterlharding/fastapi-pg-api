--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: api_credentials; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.api_credentials (
    id integer NOT NULL,
    user_id character varying(64),
    email character varying(64) NOT NULL,
    hashed_password character varying(128) NOT NULL
);


ALTER TABLE public.api_credentials OWNER TO root;

--
-- Name: api_credentials_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.api_credentials_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.api_credentials_id_seq OWNER TO root;

--
-- Name: api_credentials_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.api_credentials_id_seq OWNED BY public.api_credentials.id;


--
-- Name: application_user; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.application_user (
    id integer NOT NULL,
    user_id character varying(64) NOT NULL,
    username character varying(45) NOT NULL,
    password character varying(64) NOT NULL,
    email character varying(45) NOT NULL,
    first_name character varying(45) NOT NULL,
    last_name character varying(45) NOT NULL,
    notes text DEFAULT ''::text,
    is_admin boolean DEFAULT true,
    is_active boolean DEFAULT true,
    last_login timestamp without time zone NOT NULL,
    when_created timestamp without time zone NOT NULL,
    when_modified timestamp without time zone NOT NULL
);


ALTER TABLE public.application_user OWNER TO root;

--
-- Name: application_user_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.application_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.application_user_id_seq OWNER TO root;

--
-- Name: application_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.application_user_id_seq OWNED BY public.application_user.id;


--
-- Name: city; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.city (
    id integer NOT NULL,
    name character varying(64) NOT NULL,
    city_code character varying(5) NOT NULL,
    state_code character varying(3) NOT NULL,
    country_code character varying(2) NOT NULL,
    status character varying(8),
    notes text
);


ALTER TABLE public.city OWNER TO root;

--
-- Name: city_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.city_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.city_id_seq OWNER TO root;

--
-- Name: city_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.city_id_seq OWNED BY public.city.id;


--
-- Name: db_metadata; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.db_metadata (
    id integer NOT NULL,
    release character varying(64) NOT NULL,
    db_version character varying(64) NOT NULL,
    notes text NOT NULL,
    when_modified timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.db_metadata OWNER TO root;

--
-- Name: db_metadata_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.db_metadata_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.db_metadata_id_seq OWNER TO root;

--
-- Name: db_metadata_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.db_metadata_id_seq OWNED BY public.db_metadata.id;


--
-- Name: iso_country; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.iso_country (
    id integer NOT NULL,
    code character varying(2) NOT NULL,
    iso3 character varying(3) NOT NULL,
    num3 integer NOT NULL,
    name character varying(64) NOT NULL
);


ALTER TABLE public.iso_country OWNER TO root;

--
-- Name: iso_country_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.iso_country_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.iso_country_id_seq OWNER TO root;

--
-- Name: iso_country_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.iso_country_id_seq OWNED BY public.iso_country.id;


--
-- Name: session; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.session (
    id integer NOT NULL,
    username character varying(32),
    workstation character varying(32),
    started timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    data text
);


ALTER TABLE public.session OWNER TO root;

--
-- Name: session_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.session_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.session_id_seq OWNER TO root;

--
-- Name: session_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.session_id_seq OWNED BY public.session.id;


--
-- Name: state; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.state (
    id integer NOT NULL,
    name character varying(64) NOT NULL,
    state_code character varying(3) NOT NULL,
    country_code character varying(2) NOT NULL,
    status character varying(8),
    notes text
);


ALTER TABLE public.state OWNER TO root;

--
-- Name: state_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.state_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.state_id_seq OWNER TO root;

--
-- Name: state_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.state_id_seq OWNED BY public.state.id;


--
-- Name: token_blacklist; Type: TABLE; Schema: public; Owner: root
--

CREATE TABLE public.token_blacklist (
    id integer NOT NULL,
    token character varying(512) DEFAULT NULL::character varying,
    expiry timestamp with time zone,
    blacklisted_on timestamp with time zone
);


ALTER TABLE public.token_blacklist OWNER TO root;

--
-- Name: token_blacklist_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE public.token_blacklist_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.token_blacklist_id_seq OWNER TO root;

--
-- Name: token_blacklist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE public.token_blacklist_id_seq OWNED BY public.token_blacklist.id;


--
-- Name: api_credentials id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.api_credentials ALTER COLUMN id SET DEFAULT nextval('public.api_credentials_id_seq'::regclass);


--
-- Name: application_user id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.application_user ALTER COLUMN id SET DEFAULT nextval('public.application_user_id_seq'::regclass);


--
-- Name: city id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.city ALTER COLUMN id SET DEFAULT nextval('public.city_id_seq'::regclass);


--
-- Name: db_metadata id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.db_metadata ALTER COLUMN id SET DEFAULT nextval('public.db_metadata_id_seq'::regclass);


--
-- Name: iso_country id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.iso_country ALTER COLUMN id SET DEFAULT nextval('public.iso_country_id_seq'::regclass);


--
-- Name: session id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.session ALTER COLUMN id SET DEFAULT nextval('public.session_id_seq'::regclass);


--
-- Name: state id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.state ALTER COLUMN id SET DEFAULT nextval('public.state_id_seq'::regclass);


--
-- Name: token_blacklist id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.token_blacklist ALTER COLUMN id SET DEFAULT nextval('public.token_blacklist_id_seq'::regclass);


--
-- Data for Name: api_credentials; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.api_credentials (id, user_id, email, hashed_password) FROM stdin;
1	ff40bf6f-e202-4348-8a05-d84a9098d2d2	api@example.com	2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b
\.


--
-- Data for Name: application_user; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.application_user (id, user_id, username, password, email, first_name, last_name, notes, is_admin, is_active, last_login, when_created, when_modified) FROM stdin;
1	0009ebd2-dfef-11e8-815a-0001c01c22f7	test	2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b	demo@example.com	Demo	User	Initial setup	t	t	2022-09-22 13:25:09.561203	2022-09-22 13:25:09.561203	2022-09-22 13:25:09.561203
\.


--
-- Data for Name: city; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.city (id, name, city_code, state_code, country_code, status, notes) FROM stdin;
1	New York	NY	NY	US	\N	\N
2	Sydney	SYD	NSW	AU	\N	\N
3	Melbourne	MEL	VIC	AU	\N	\N
4	Brisbane	BNE	QLD	AU	\N	\N
5	Adelaide	ADL	SA	AU	\N	\N
6	Canberra	CAN	ACT	AU	\N	\N
7	Hobart	HBT	TAS	AU	\N	\N
8	Perth	PER	WA	AU	\N	\N
9	Darwin	DWN	NT	AU	\N	\N
\.


--
-- Data for Name: db_metadata; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.db_metadata (id, release, db_version, notes, when_modified) FROM stdin;
1	test	v1.0.0	Promote to released.	2020-11-17 02:07:45.174652
\.


--
-- Data for Name: iso_country; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.iso_country (id, code, iso3, num3, name) FROM stdin;
1	AF	AFG	4	Afghanistan
2	AX	ALA	248	Aland Islands
3	AL	ALB	8	Albania
4	DZ	DZA	12	Algeria
5	AS	ASM	16	American Samoa
6	AD	AND	20	Andorra
7	AO	AGO	24	Angola
8	AI	AIA	660	Anguilla
9	AQ	ATA	10	Antarctica
10	AG	ATG	28	Antigua and Barbuda
11	AR	ARG	32	Argentina
12	AM	ARM	51	Armenia
13	AW	ABW	533	Aruba
14	AU	AUS	36	Australia
15	AT	AUT	40	Austria
16	AZ	AZE	31	Azerbaijan
17	BS	BHS	44	Bahamas
18	BH	BHR	48	Bahrain
19	BD	BGD	50	Bangladesh
20	BB	BRB	52	Barbados
21	BY	BLR	112	Belarus
22	BE	BEL	56	Belgium
23	BZ	BLZ	84	Belize
24	BJ	BEN	204	Benin
25	BM	BMU	60	Bermuda
26	BT	BTN	64	Bhutan
27	BO	BOL	68	Bolivia
28	BA	BIH	70	Bosnia and Herzegovina
29	BW	BWA	72	Botswana
30	BV	BVT	74	Bouvet Island
31	BR	BRA	76	Brazil
32	IO	IOT	86	British Indian Ocean Territory
33	BN	BRN	96	Brunei Darussalam
34	BG	BGR	100	Bulgaria
35	BF	BFA	854	Burkina Faso
36	BI	BDI	108	Burundi
37	KH	KHM	116	Cambodia
38	CM	CMR	120	Cameroon
39	CA	CAN	124	Canada
40	CV	CPV	132	Cape Verde
41	KY	CYM	136	Cayman Islands
42	CF	CAF	140	Central African Republic
43	TD	TCD	148	Chad
44	CL	CHL	152	Chile
45	CN	CHN	156	China
46	CX	CXR	162	Christmas Island
47	CC	CCK	166	Cocos (Keeling) Islands
48	CO	COL	170	Colombia
49	KM	COM	174	Comoros
50	CG	COG	178	Congo
51	CD	COD	180	Congo, Democratic Republic of the
52	CK	COK	184	Cook Islands
53	CR	CRI	188	Costa Rica
54	CI	CIV	384	Cote d'Ivoire
55	HR	HRV	191	Croatia
56	CU	CUB	192	Cuba
57	CY	CYP	196	Cyprus
58	CZ	CZE	203	Czech Republic
59	DK	DNK	208	Denmark
60	DJ	DJI	262	Djibouti
61	DM	DMA	212	Dominica
62	DO	DOM	214	Dominican Republic
63	EC	ECU	218	Ecuador
64	EG	EGY	818	Egypt
65	SV	SLV	222	El Salvador
66	GQ	GNQ	226	Equatorial Guinea
67	ER	ERI	232	Eritrea
68	EE	EST	233	Estonia
69	ET	ETH	231	Ethiopia
70	FK	FLK	238	Falkland Islands (Malvinas)
71	FO	FRO	234	Faroe Islands
72	FJ	FJI	242	Fiji
73	FI	FIN	246	Finland
74	FR	FRA	250	France
75	GF	GUF	254	French Guiana
76	PF	PYF	258	French Polynesia
77	TF	ATF	260	French Southern Territories
78	GA	GAB	266	Gabon
79	GM	GMB	270	Gambia
80	GE	GEO	268	Georgia
81	DE	DEU	276	Germany
82	GH	GHA	288	Ghana
83	GI	GIB	292	Gibraltar
84	GR	GRC	300	Greece
85	GL	GRL	304	Greenland
86	GD	GRD	308	Grenada
87	GP	GLP	312	Guadeloupe
88	GU	GUM	316	Guam
89	GT	GTM	320	Guatemala
90	GG	GGY	831	Guernsey Guernsey
91	GN	GIN	324	Guinea
92	GW	GNB	624	Guinea-Bissau
93	GY	GUY	328	Guyana
94	HT	HTI	332	Haiti
95	HM	HMD	334	Heard Island and McDonald Islands
96	VA	VAT	336	Holy See (Vatican City State)
97	HN	HND	340	Honduras
98	HK	HKG	344	Hong Kong
99	HU	HUN	348	Hungary
100	IS	ISL	352	Iceland
101	IN	IND	356	India
102	ID	IDN	360	Indonesia
103	IR	IRN	364	Iran, Islamic Republic of
104	IQ	IRQ	368	Iraq
105	IE	IRL	372	Ireland
106	IM	IMN	833	Isle of Man
107	IL	ISR	376	Israel
108	IT	ITA	380	Italy
109	JM	JAM	388	Jamaica
110	JP	JPN	392	Japan
111	JE	JEY	832	Jersey
112	JO	JOR	400	Jordan
113	KZ	KAZ	398	Kazakhstan
114	KE	KEN	404	Kenya
115	KI	KIR	296	Kiribati
116	KP	PRK	408	Korea, Democratic People's Republic of
117	KR	KOR	410	Korea, Republic of
118	KW	KWT	414	Kuwait
119	KG	KGZ	417	Kyrgyzstan
120	LA	LAO	418	Lao People's Democratic Republic
121	LV	LVA	428	Latvia
122	LB	LBN	422	Lebanon
123	LS	LSO	426	Lesotho
124	LR	LBR	430	Liberia
125	LY	LBY	434	Libya Libyan Arab Jamahiriya
126	LI	LIE	438	Liechtenstein
127	LT	LTU	440	Lithuania
128	LU	LUX	442	Luxembourg
129	MO	MAC	446	Macao
130	MK	MKD	807	Macedonia, the former Yugoslav Republic of
131	MG	MDG	450	Madagascar
132	MW	MWI	454	Malawi
133	MY	MYS	458	Malaysia
134	MV	MDV	462	Maldives
135	ML	MLI	466	Mali
136	MT	MLT	470	Malta
137	MH	MHL	584	Marshall Islands
138	MQ	MTQ	474	Martinique
139	MR	MRT	478	Mauritania
140	MU	MUS	480	Mauritius
141	YT	MYT	175	Mayotte
142	MX	MEX	484	Mexico
143	FM	FSM	583	Micronesia, Federated States of
144	MD	MDA	498	Moldova, Republic of
145	MC	MCO	492	Monaco
146	MN	MNG	496	Mongolia
147	ME	MNE	499	Montenegro
148	MS	MSR	500	Montserrat
149	MA	MAR	504	Morocco
150	MZ	MOZ	508	Mozambique
151	MM	MMR	104	Myanmar
152	NA	NAM	516	Namibia
153	NR	NRU	520	Nauru
154	NP	NPL	524	Nepal
155	NL	NLD	528	Netherlands
156	AN	ANT	530	Netherlands Antilles
157	NC	NCL	540	New Caledonia
158	NZ	NZL	554	New Zealand
159	NI	NIC	558	Nicaragua
160	NE	NER	562	Niger
161	NG	NGA	566	Nigeria
162	NU	NIU	570	Niue
163	NF	NFK	574	Norfolk Island
164	MP	MNP	580	Northern Mariana Islands
165	NO	NOR	578	Norway
166	OM	OMN	512	Oman
167	PK	PAK	586	Pakistan
168	PW	PLW	585	Palau
169	PS	PSE	275	Palestinian Territory, Occupied
170	PA	PAN	591	Panama
171	PG	PNG	598	Papua New Guinea
172	PY	PRY	600	Paraguay
173	PE	PER	604	Peru
174	PH	PHL	608	Philippines
175	PN	PCN	612	Pitcairn
176	PL	POL	616	Poland
177	PT	PRT	620	Portugal
178	PR	PRI	630	Puerto Rico
179	QA	QAT	634	Qatar
180	RE	REU	638	Reunion
181	RO	ROU	642	Romania
182	RU	RUS	643	Russian Federation
183	RW	RWA	646	Rwanda
184	SH	SHN	654	Saint Helena
185	KN	KNA	659	Saint Kitts and Nevis
186	LC	LCA	662	Saint Lucia
187	PM	SPM	666	Saint Pierre and Miquelon
188	VC	VCT	670	Saint Vincent and the Grenadines
189	WS	WSM	882	Samoa
190	SM	SMR	674	San Marino
191	ST	STP	678	Sao Tome and Principe
192	SA	SAU	682	Saudi Arabia
193	SN	SEN	686	Senegal
194	RS	SRB	688	Serbia
195	SC	SYC	690	Seychelles
196	SL	SLE	694	Sierra Leone
197	SG	SGP	702	Singapore
198	SK	SVK	703	Slovakia
199	SI	SVN	705	Slovenia
200	SB	SLB	90	Solomon Islands
201	SO	SOM	706	Somalia
202	ZA	ZAF	710	South Africa
203	GS	SGS	239	South Georgia and the South Sandwich Islands
204	ES	ESP	724	Spain
205	LK	LKA	144	Sri Lanka
206	SD	SDN	736	Sudan
207	SR	SUR	740	Suriname
208	SJ	SJM	744	Svalbard and Jan Mayen
209	SZ	SWZ	748	Swaziland
210	SE	SWE	752	Sweden
211	CH	CHE	756	Switzerland
212	SY	SYR	760	Syrian Arab Republic
213	TW	TWN	158	Taiwan, Province of China
214	TJ	TJK	762	Tajikistan
215	TZ	TZA	834	Tanzania, United Republic of
216	TH	THA	764	Thailand
217	TL	TLS	626	Timor-Leste
218	TG	TGO	768	Togo
219	TK	TKL	772	Tokelau
220	TO	TON	776	Tonga
221	TT	TTO	780	Trinidad and Tobago
222	TN	TUN	788	Tunisia
223	TR	TUR	792	Turkey
224	TM	TKM	795	Turkmenistan
225	TC	TCA	796	Turks and Caicos Islands
226	TV	TUV	798	Tuvalu
227	UG	UGA	800	Uganda
228	UA	UKR	804	Ukraine
229	AE	ARE	784	United Arab Emirates
230	GB	GBR	826	United Kingdom
231	US	USA	840	United States
232	UM	UMI	581	United States Minor Outlying Islands
233	UY	URY	858	Uruguay
234	UZ	UZB	860	Uzbekistan
235	VU	VUT	548	Vanuatu
236	VE	VEN	862	Venezuela
237	VN	VNM	704	Viet Nam
238	VG	VGB	92	Virgin Islands, British
239	VI	VIR	850	Virgin Islands, U.S.
240	WF	WLF	876	Wallis and Futuna
241	EH	ESH	732	Western Sahara
242	YE	YEM	887	Yemen
243	ZM	ZMB	894	Zambia
244	ZW	ZWE	716	Zimbabwe
\.


--
-- Data for Name: session; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.session (id, username, workstation, started, data) FROM stdin;
1	test	192.168.100.152	2022-09-23 00:00:42.420703	0009ebd2-dfef-11e8-815a-0001c01c22f7
2	test	192.168.100.152	2022-09-23 00:02:45.397634	0009ebd2-dfef-11e8-815a-0001c01c22f7
3	test	192.168.100.152	2022-09-23 00:04:33.857389	0009ebd2-dfef-11e8-815a-0001c01c22f7
4	test	192.168.100.152	2022-09-23 00:06:10.301574	0009ebd2-dfef-11e8-815a-0001c01c22f7
5	test	192.168.100.152	2022-09-23 00:07:16.052036	0009ebd2-dfef-11e8-815a-0001c01c22f7
6	test	192.168.100.152	2022-09-23 00:09:57.297596	0009ebd2-dfef-11e8-815a-0001c01c22f7
\.


--
-- Data for Name: state; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.state (id, name, state_code, country_code, status, notes) FROM stdin;
1	New South Wales	NSW	AU	\N	\N
2	Victoria	VIC	AU	\N	\N
3	Queensland	QLD	AU	\N	\N
4	Australian Capital Territory	ACT	AU	\N	\N
5	South Australia	SA	AU	\N	\N
6	Western Australia	WA	AU	\N	\N
7	Tasmania	TAS	AU	\N	\N
8	Northern Territory	NT	AU	\N	\N
9	Alabama	AL	US	\N	\N
10	Alaska	AK	US	\N	\N
11	Arizona	AZ	US	\N	\N
12	Arkansas	AR	US	\N	\N
13	California	CA	US	\N	\N
14	Colorado	CO	US	\N	\N
15	Connecticut	CT	US	\N	\N
16	Delaware	DE	US	\N	\N
17	Florida	FL	US	\N	\N
18	Georgia	GA	US	\N	\N
19	Hawaii	HI	US	\N	\N
20	Idaho	ID	US	\N	\N
21	Illinois	IL	US	\N	\N
22	Indiana	IN	US	\N	\N
23	Iowa	IA	US	\N	\N
24	Kansas	KS	US	\N	\N
25	Kentucky	KY	US	\N	\N
26	Louisiana	LA	US	\N	\N
27	Maine	ME	US	\N	\N
28	Maryland	MD	US	\N	\N
29	Massachusetts	MA	US	\N	\N
30	Michigan	MI	US	\N	\N
31	Minnesota	MN	US	\N	\N
32	Mississippi	MS	US	\N	\N
33	Missouri	MO	US	\N	\N
34	Montana	MT	US	\N	\N
35	Nebraska	NE	US	\N	\N
36	Nevada	NV	US	\N	\N
37	New Hampshire	NH	US	\N	\N
38	New Jersey	NJ	US	\N	\N
39	New Mexico	NM	US	\N	\N
40	New York	NY	US	\N	\N
41	North Carolina	NC	US	\N	\N
42	North Dakota	ND	US	\N	\N
43	Ohio	OH	US	\N	\N
44	Oklahoma	OK	US	\N	\N
45	Oregon	OR	US	\N	\N
46	Pennsylvania	PA	US	\N	\N
47	Rhode Island	RI	US	\N	\N
48	South Carolina	SC	US	\N	\N
49	South Dakota	SD	US	\N	\N
50	Tennessee	TN	US	\N	\N
51	Texas	TX	US	\N	\N
52	Utah	UT	US	\N	\N
53	Vermont	VT	US	\N	\N
54	Virginia	VA	US	\N	\N
55	Washington	WA	US	\N	\N
56	West Virginia	WV	US	\N	\N
57	Wisconsin	WI	US	\N	\N
58	Wyoming	WY	US	\N	\N
59	American Samoa	AS	US	\N	\N
60	District of Columbia	DC	US	\N	\N
61	Federated States of Micronesia	FM	US	\N	\N
62	Guam	GU	US	\N	\N
63	Marshall Islands	MH	US	\N	\N
64	Northern Mariana Islands	MP	US	\N	\N
65	Palau	PW	US	\N	\N
66	Puerto Rico	PR	US	\N	\N
67	Virgin Islands	VI	US	\N	\N
\.


--
-- Data for Name: token_blacklist; Type: TABLE DATA; Schema: public; Owner: root
--

COPY public.token_blacklist (id, token, expiry, blacklisted_on) FROM stdin;
\.


--
-- Name: api_credentials_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.api_credentials_id_seq', 1, false);


--
-- Name: application_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.application_user_id_seq', 1, false);


--
-- Name: city_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.city_id_seq', 1, false);


--
-- Name: db_metadata_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.db_metadata_id_seq', 1, false);


--
-- Name: iso_country_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.iso_country_id_seq', 244, true);


--
-- Name: session_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.session_id_seq', 1, false);


--
-- Name: state_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.state_id_seq', 1, false);


--
-- Name: token_blacklist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('public.token_blacklist_id_seq', 1, false);


--
-- Name: api_credentials api_credentials_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.api_credentials
    ADD CONSTRAINT api_credentials_pkey PRIMARY KEY (id);


--
-- Name: application_user application_user_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.application_user
    ADD CONSTRAINT application_user_pkey PRIMARY KEY (id);


--
-- Name: application_user application_user_user_id_key; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.application_user
    ADD CONSTRAINT application_user_user_id_key UNIQUE (user_id);


--
-- Name: application_user application_user_username_key; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.application_user
    ADD CONSTRAINT application_user_username_key UNIQUE (username);


--
-- Name: city city_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.city
    ADD CONSTRAINT city_pkey PRIMARY KEY (id);


--
-- Name: db_metadata db_metadata_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.db_metadata
    ADD CONSTRAINT db_metadata_pkey PRIMARY KEY (id);


--
-- Name: iso_country iso_country_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.iso_country
    ADD CONSTRAINT iso_country_pkey PRIMARY KEY (id);


--
-- Name: session session_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.session
    ADD CONSTRAINT session_pkey PRIMARY KEY (id);


--
-- Name: state state_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.state
    ADD CONSTRAINT state_pkey PRIMARY KEY (id);


--
-- Name: token_blacklist token_blacklist_pkey; Type: CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY public.token_blacklist
    ADD CONSTRAINT token_blacklist_pkey PRIMARY KEY (id);


--
-- Name: TABLE api_credentials; Type: ACL; Schema: public; Owner: root
--

GRANT ALL ON TABLE public.api_credentials TO api;


--
-- Name: TABLE application_user; Type: ACL; Schema: public; Owner: root
--

GRANT ALL ON TABLE public.application_user TO api;


--
-- Name: TABLE city; Type: ACL; Schema: public; Owner: root
--

GRANT ALL ON TABLE public.city TO api;


--
-- Name: TABLE db_metadata; Type: ACL; Schema: public; Owner: root
--

GRANT ALL ON TABLE public.db_metadata TO api;


--
-- Name: TABLE iso_country; Type: ACL; Schema: public; Owner: root
--

GRANT ALL ON TABLE public.iso_country TO api;


--
-- Name: TABLE session; Type: ACL; Schema: public; Owner: root
--

GRANT ALL ON TABLE public.session TO api;


--
-- Name: TABLE state; Type: ACL; Schema: public; Owner: root
--

GRANT ALL ON TABLE public.state TO api;


--
-- Name: TABLE token_blacklist; Type: ACL; Schema: public; Owner: root
--

GRANT ALL ON TABLE public.token_blacklist TO api;


--
-- PostgreSQL database dump complete
--

