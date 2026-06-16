---
title: Knowledge Graphs for AI Agents (A Practical Guide)
video_id: clhZES0M7no
url: https://www.youtube.com/watch?v=clhZES0M7no
channel: SurrealDB
channel_id: UCjf2teVEuYVvvVC-gFZNq6w
channel_url: https://www.youtube.com/channel/UCjf2teVEuYVvvVC-gFZNq6w
publish_date: '2026-04-27T09:16:20-07:00'
upload_date: '2026-04-27T09:16:20-07:00'
category: Science & Technology
duration: '1:00:04'
length_seconds: 3604
view_count: 3385
is_live: false
thumbnail: https://i.ytimg.com/vi_webp/clhZES0M7no/maxresdefault.webp
caption_tracks:
- language_code: en
  name: English
  kind: manual
  is_translatable: true
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
chapters:
- title: Intro
  start: 0:00
  start_ms: 0
- title: What is a Knowledge Graph?
  start: '3:55'
  start_ms: 235000
- title: Why vector-only RAG breaks
  start: '11:19'
  start_ms: 679000
- title: 'Q&A: How GraphRAG actually works'
  start: '21:48'
  start_ms: 1308000
- title: 'Building a KG: Extract, Transform, Load'
  start: '25:13'
  start_ms: 1513000
- title: 'Demo: exploring a KG in Surrealist'
  start: '43:23'
  start_ms: 2603000
- title: Agentic RAG & tool calling
  start: '46:49'
  start_ms: 2809000
- title: 'One query: vector + graph in SurrealQL'
  start: '50:38'
  start_ms: 3038000
- title: Wrap-up
  start: '58:31'
  start_ms: 3511000
description: |-
  👉 RAG systems hit a wall as they scale: dense vector neighbourhoods produce context clash, hallucinations creep into answers, and high-dimensional embeddings stop being enough on their own. This session uses real-world examples — e-commerce search, customer support, agentic chatbots — to analyse where vector-only RAG breaks down, and the operational cost of stitching together separate vector, graph, and full-text stores. Martin (Solutions Engineer at SurrealDB) demonstrates how knowledge graphs ground LLM responses by adding deterministic structure on top of vectors, walking through the full ETL pipeline — parsing, chunking, embedding, entity and relationship extraction, deduplication, ontology alignment, and loading — and shows how a single SurrealQL query can combine vector search, multi-hop graph traversal, and full-text search to serve agentic RAG from one live dataset, avoiding the architectural "duct tape" of multi-database glue code.

  🖥️ Explore other SurrealDB webinars: https://sdb.li/4sOML5J
  📃 Read the guide: https://sdb.li/3R3p6RG

  --- Chapters ---
  00:00 Intro
  03:55 What is a Knowledge Graph?
  11:19 Why vector-only RAG breaks
  21:48 Q&A: How GraphRAG actually works
  25:13 Building a KG: Extract, Transform, Load
  43:23 Demo: exploring a KG in Surrealist
  46:49 Agentic RAG & tool calling
  50:38 One query: vector + graph in SurrealQL
  58:31 Wrap-up

  --- Resources ---
  ☁️  Start free on Surreal Cloud: https://surrealdb.com/cloud
  🎓  SurrealDB University: https://surrealdb.com/learn
  📚  Docs: https://surrealdb.com/docs
  🎩  Surrealist (GUI): https://surrealdb.com/surrealist
  ⭐️  GitHub: https://github.com/surrealdb/surrealdb

  --- What is SurrealDB? ---
  SurrealDB is an AI-native, multi-model database built in Rust that unifies document, graph, time-series, relational, geospatial and key-value data models into a single engine. Combined with powerful search and retrieval (vector, full-text, hybrid), real-time and event-driven capabilities, and Spectron - its persistent memory layer for AI agents - SurrealDB provides the complete context layer so that models run next to the data, context remains synchronised, and application logic stays simple and dependable.

  --- Connect ---
  🐦  Twitter: https://twitter.com/surrealdb
  👩‍💻  LinkedIn: https://www.linkedin.com/company/surrealdb/
  💬  Discord: https://discord.com/invite/surrealdb
  🛍️  Merch: https://surrealdb.store/
notes: |-
  Transcript fetched via youtube-transcript-api fallback after the Playwright path hit 'transcript panel did not render' timeout (GH #2). Video has TWO caption tracks: manual (kind=manual) and ASR (kind=asr); picked the MANUAL track for highest fidelity. Light cleanup: dropped [music]/[applause]/[beeping] non-speech markers, grouped consecutive segments into ~12-second windows with [mm:ss] timestamps, speaker-turn breaks (manual track preserves speaker labels in caps). 728 raw segments -> N grouped windows (replace N after run).
---

## [0:00] Intro
[0:08] I'm Martin, solutions engineer at SurrealDB. I'll be talking today about knowledge graphs for AI agents. Keep an eye on the chat on the right. Make sure you
[0:23] add any questions you have. We'll be responding them, in the chat. And, yeah, also, I see familiar faces there in the chat already. Hi, Santi. And, yeah, let us know where you're connecting
[0:38] from. And, yeah, if you have any questions, feel free to ask. Cool. And, yeah, while more people connect, let's let's get started.
[0:51] So first, a quick introduction about SurrealDB. SurrealDB was opens became open source in GitHub maybe around three year two three years already.
[1:04] It become became very popular on the Rust community. It was featured in a couple of YouTube videos back then, and, yeah, it got a lot of traction.
[1:20] And I started using it actually, like, three years ago already, and yeah, never stopped since. We are almost reaching 31k stars on GitHub. I think we're already there.
[1:35] We've had some traction in the enterprise customers. We've been deployed in embedded systems, on the edge, highly distributed architectures.
[1:48] It's it's yeah, a very like, flexible database to deploy. It was built, on Rust, so it can be compiled to different architectures
[2:05] which allows it to run embedded even in the browser or in highly distributed environments. It's multimodal which means in the same engine, you have all the modalities you can think of, like
[2:25] relational tables, also document tables, like any JSON blob you want to store. You also have time series, geospatial so you can query coordinates, for example. You have vector search
[2:40] which is very common now in AI use cases full text search that enables you hybrid search together with full text search and, key value, of course. And then graph is one of the most
[2:56] common ones now for AI use cases as well. And so it's very common to mix graph, full text search, and vector search when you are doing RAG systems, for example. And so it's very convenient to use SurrealDB because you only have one database
[3:11] to hold all those three modalities while relational and document are also very popular, also within RAG use cases. We have also some AI here and machine learning here
[3:25] because you can actually if you go down the path, you can actually import ML models into SurrealDB and have
[3:38] some inference functions running while you, for example, insert a new record. You can, do, like, sentiment analysis and things like that with your custom ML models.
[3:52] And yeah. So that's SurrealDB, at a glance.

## [3:55] What is a Knowledge Graph?
[3:56] So let's get into the topic of knowledge graphs. So what is a knowledge graph? Let's start with with the formal definition taken from Wikipedia
[4:11] also to demonstrate that knowledge graphs is actually not a new thing now in the AI use cases. This became very popular a couple of decades ago already and was very popular in the Google
[4:25] search engine, for example, so that it keeps like, concepts related so that your results are more valuable in that sense. It represents and operates on data. Right? So
[4:40] basically, the graph is a representation of your knowledge where you have concepts related to other concepts or entities related to entities using different types of relationships. But, of course, it not only stores data, but it also
[4:55] is used to navigate your knowledge graph. Right? So when we talk about doing multi hop graphs, it's basically you're navigating the graph hopping from one entity to another to a specific relationship and can do home
[5:13] many hops, as you like, depending, again, on your use case. It also, allows you to keep it updated very easily, which is
[5:27] one of the nice things of using a knowledge graph together with a vector store because a knowledge graph is very easy to update especially if you, for example, take decisions based on some knowledge you may have in your
[5:40] graph. Then you can actually reflect that back. And in the future, you can have also, like, a bit of traceability. In general, I think knowledge graph, it's it's a tool that allows you to be very
[5:55] creative to solve your RAG issues or and also to can kind of represent different information that is sometimes not as easy to represent when you only have vector stores, for example.
[6:11] So let's start first by knowledge graphs, and and I want to show two different specimens to contrast one with each, with the other. Because in this area, in this topic about how to build a knowledge graph
[6:26] it actually depends a lot on two things. First, the your dataset. Yeah. There's a lot of different types of datasets. And on the other hand, your use cases.
[6:38] Right? So depends on your dataset, the nature of your data, and the nature of your use case or let's think about the types of questions a user is going to ask your chatbot.
[6:51] Then depending on those two things, the way you build your knowledge graph, it can be very different. And, also, in some cases, maybe a knowledge graph is not the ideal solution. It's
[7:03] sometimes not enough and some sometimes just an overkill. And so on one side, we have knowledge curve like this, which is generated from very explicit data in your database. So for example
[7:21] assume you have an ecommerce database where you have tables mostly relational data, with transactional data as well, where you have products that are part of categories.
[7:37] Then a product may have, reviews, and a product also may have an order. Right? So every time a customer creates an order, then there is a relationship between that order and the product.
[7:50] And that also contains some metadata, like how many items were sold in that specific order. And then below orders, you may have, like, customers or any other types of relations. So here, for example, if you generate a graph like this from
[8:07] transactional data, it's very obvious what your entities and relationships are. Right? It's more mostly like a map from your relational data into your knowledge graph.
[8:20] On the other hand, you can have, more graphs that are not as explicit in your original dataset and that you may need an LLM to infer some of the entities and some of the relationships as well.
[8:35] This one is a hybrid because you have things that are very explicit in your data, like, for example, the author of an article or a document and the year may be also very explicit in the header of the document.
[8:53] But chunks, concepts, and probably companies are things that are going to be inferred by an LLM, like analyzing the document or just specific chunks.
[9:06] And then the relationships as well, like, for example, leader in that relates company with concepts. Actually, this one may be different. Like, probably, like, a concept like
[9:18] a yeah. Maybe this is like, a company's leader in a specific solution or a specific industry. Right? So concepts will hold industries, for example, and then a company would be a leader of that industry, which is something that the LLM
[9:34] inferred from that company, coming from a specific, like, document chunk. So as you can see, yeah, some of these relationships and entities can be inferred
[9:47] are not very explicit on the dataset. And but then, coming back to the other thing you need to have in mind is your use case. Right? What's for example, if you're building a chatbot to do RAG
[10:02] what are the questions that your users are going to ask? Right? So do you need to actually, identify concepts, companies, chunks, years? Right? So for example, if you are in, building a chatbot for customer support and you
[10:18] are generating a graph from support, troubleshooting emails or Slack messages or whatever and you want to, in the future, respond to some of
[10:33] the same questions, then probably you would want to generate an inferred graph where you can hold like, the product the question is about probably even the version of the software the user is running.
[10:49] And then you also want to infer, like, if a step in the troubleshooting process what's actually a solution or not so that you can
[11:05] mark solutions in the in the knowledge graph, as, like good solutions or just bad troubleshooting steps and so on. So it really depends
[11:18] on your use case. So, why do AI agents need knowledge graphs? Right?

## [11:19] Why vector-only RAG breaks
[11:24] Sometimes I get this question and people are, argue that maybe a good vector story with very high dimensional, vectors are good enough. And sometimes, yeah, it's true. Right? Sometimes
[11:41] a vector story is just enough, to build the right context for your chatbot to be able to generate a good answer. Right? But sometimes what I've seen is that at scale, vector store
[11:58] Vector stores get you probably a lot of chunks with a high accuracy, but they basically compete with each other. So sometimes you have
[12:11] context clash or even context confusion where the LLM just gets a lot of of, chunks to generate an answer, but maybe there are too many chunks. All could can be correct, but there are maybe too many chunks.
[12:27] And sometimes LLMs don't like big context and things that look like can contradict themselves. So that's where, knowledge graphs come into play
[12:39] because they allow you to be more deterministic and also, like, to trim down, like, defector space so that, you can more accurately give the LLM just a very specific
[12:54] chunks of data that are required to generate an answer. In this case, this is a nice analogy. I think LLMs are very good storytellers. They're very good at generating an answer.
[13:09] But if they don't have any, like, factual data or context from your RAG system. Right? If it they don't have, like, facts or good context
[13:23] they are just going to hallucinate an answer. So the idea is to put them together. Right? So have a very good storyteller generating answers, but a very good
[13:36] knowledge graph that as deterministic as possible generates good contexts for the LLM to generate a nice a nice, story.
[13:52] In this case, yeah, for example, we want we have the previous knowledge graph as an example where you have reviews for products that are part of an order. So it's very easy and
[14:04] and very deterministic to get the best seller products from your knowledge graph. Right? Because it's just relations and metadata give you the latest the orders from this
[14:19] month, then the best seller products. So if you run this query, you're going to build a very accurate deterministic context for you, LLM, to summarize all those all those reviews.
[14:36] And just to make it clearer if you imagine this without a knowledge graph and only using vector stores, from the vector store, you may get summaries
[14:52] that are semantically close to to the question. So somehow, it's going to give you an answer, but it's going to completely hallucinate, what the most popular products in your store are. Right?
[15:09] And if you have a very big vector store with a lot of information from your company, maybe it's already ingested, like slides or presentations or even conversations from your
[15:24] internal Slack or internal Notion pages where there is some information about this month's best seller products. So it's actually possible that using only Vector store
[15:36] it can actually find this information if the information is somewhere in that vector store. But it's not going to be very accurate and definitely not deterministic. Right? And it also would require some human to actually have presented
[15:53] about the best seller products of this month so that information goes somewhere and gets ingested in your vector store. But if you have a knowledge graph like this, which is hopefully even the same
[16:08] database as your transactional data, it means that this will be just completely up to date, and it will be very deterministic way to get the best of our products and then summarize the best reviews.
[16:24] So definitely no chance for an hallucinations in that in that use case. And going back to, vector embeddings, as I said, if you have very big
[16:38] vector space, you may have very very dense neighborhoods. Like you can see in this diagram, imagine you get a lot of documents or chunks
[16:52] inserted in the same very specific neighborhood in your vector store probably because they're talking about the same topic and you get more and more and more chunks very close by. It means that when there
[17:06] never there is a query that is also positioned in that specific point in the vector space, it's there's a high chance to get a lot of results from a vector query. Right?
[17:20] So it's going to start, having issues by picking which is the best chunk to use to generate an answer. So adding graph to that helps you trim down the results.
[17:35] So imagine you create relationships between some of those nodes. Again, I'm assuming we are in. So you have vectors and graphs in the same
[17:49] data, in the same records. So a single node can be vector embedded and will be connected to different nodes through different relationships. So it means that you can, like, do a vector search query
[18:04] but use their graph relationships to trim it down. Right? So, for example if you are in customer support or product support. Right? Someone is asking about
[18:16] that my mouse is not working. Right? Like how do I troubleshoot Bluetooth issues, for example? So from the prompt, you can infer the product and the issue. Right? It's it's a mouse, and it's related to Bluetooth.
[18:32] So you could have that represented in your knowledge graph. So, for example all the notes with troubleshooting guides and resolutions to issues that are ingested in your store can be related to the specific domains and
[18:48] products. So, basically, all those chunks that are related to Bluetooth issues for your mouse would be also connected to the graph node that is about that specific product
[19:02] and also specific to troubleshooting guides. So you can do a query to the vector store, but trimming out or just including in only the nodes in the vector space that have a relationship
[19:16] to the mouse product and also to troubleshooting information which will then reduce a lot the vector space. And then these high dense neighborhoods are going to be less dense, and then it will be easier to get a very
[19:32] accurate response. And, also, you know, you're only taking into consideration chunks that are related to a specific product and to the specific domain of troubleshooting articles.
[19:46] So it's not going to have a lot of context clash in that sense. Yep. This is basically a lot of what I was telling.
[20:00] There is no right or wrong way or easy way to say if you are good to go only with vector, only with graph, with both, or even
[20:13] a full text search to the mix. But as a rule of thumb, if your agent just needs to answer questions based on the manual, like troubleshooting or customer support, Vector Store could be enough.
[20:27] Depends on the scale and depends on if you have a a lot of products, a lot of domains, a lot of things in the same store. And that's typically what you would use only in the vector stores for. But if your
[20:41] agent needs to make decisions follow policies, or manage complex workflows, then definitely you would need a knowledge graph, especially if you need, like, explainability or traceability
[20:57] related to those decisions. And sometimes or probably a lot of the times, actually, if you're in a use case where you're taking decisions, maybe you're also storing them back
[21:10] in the knowledge graph to inform future decisions as well. So in that case, if your knowledge is also very dynamic and you want future
[21:23] retrievals to be related to previous retrievals, and definitely, you also need a knowledge graph. Cool. Let's see if there is any questions there.
[21:44] Yes. There is a question from Sebastian.

## [21:48] Q&A: How GraphRAG actually works
[21:48] Hello I would like to know how GraphRAG works. Is it basically a nested SQL query with let's say, three helps document page section plus embedding?
[22:02] Yes. So not I don't want to move my slides forward just in case of the of the spoilers. But with SurrealDB, you can do a single query
[22:15] that, for example, you can do a vector query to find the nearest node from your prompt. And from there, you can, in the same
[22:29] query, like, get siblings. Right? So for example, if you have a specific relationship coming out of that node that is embedded, then you can do that hop to the siblings in the graph.
[22:45] So for example, you can get to a chunk based on vector search. So you get the chunks that are similar to your original vector, the prompt vector prompt. And then you can get very easily, for example, the related documents
[23:01] by doing a graph, relation by navigating through a graph relation. And but, of course, you can do multi hops. You can not only get the document that is connected to your chunk, but also, like, concepts
[23:15] that are connected to your chunk. And the relationships of also will be very important. Right? Because, concept could be could be related by a relationship that explains
[23:28] the concept, with the chunk or a relationship that is not, like, an explain like, concept explains chunk, but maybe it's
[23:43] an author that wrote the article or a possible possible reference to a product. Right?
[23:59] So, yeah, hopefully, I, answered the question. But if not hopefully, going to have time to show some example queries that are sometimes pretty long. And but it's
[24:14] the beauty of having our own SQL like query language is that we can have all those modalities in a single query. But, also, we have nice, like, array and object functions that allow you to even
[24:31] build a nice JSON format as and give that as an output of the of the query. It can be as complex as you want. And trust me, I've seen queries that are
[24:44] very complex in a good way, because people get very creative. So it's usually the simplest form of hybrid queries have been when you combine full text search with vector.
[25:01] But I've seen, like, multi hybrid queries where you can combine full text search with vector, with graph and even relationships and everything in a single query.

## [25:13] Building a KG: Extract, Transform, Load
[25:13] And do even the re ranking and deduct deducting data in the same query. So, yeah, let's let's get to that point and show some sample queries.
[25:25] Continuing with how to build a knowledge graph, it's basically an ETL process. E is for extraction, t for transform, and l for loading. So let's keep that popular
[25:41] acronym, and let's dive into it. So extraction is about parsing, chunking, embedding and entity and relationship extraction. Right? So, and there is a lot of use cases. So some use
[25:57] cases don't need you to parse data. But imagine the worst case scenario where you have a PDF that has images, tables text, figures, everything. Right? So it's a multimodal PDF.
[26:12] So you definitely need to parse it to translate the PDF into readable, text. Like, I mean, like, plain text, readable for an LLM. So the issue there is that if the PDF has images
[26:28] you need to decide what you want to do with the images so you can caption the images. And then in the plain text, you add the caption of the image so that the LLM
[26:40] when it reads the text, knows that there was supposed to be an image, and then it will read what the image is about instead of actually reading the the rasterized image. Right? So it's you
[26:53] just translate the images into captions. That works in some cases. In some other cases, you want to actually have the real image and have an LLM be able to see the image. Right?
[27:06] And in some other cases, the opposite. You can just remove the images and forget about them. Right? In some cases. Right? So that's, I think, the worst case scenario where you have multimodal PDFs
[27:21] and tables. You can also have tables within PDFs. And tables are also very tricky. But, again, depends on the use case. Then chunking is, the process of making
[27:35] text just readable, like, smaller so that you can actually read it and in within the context window. So what LLMs cannot you cannot pass a 100 page long PDF to an LLM and ask a question.
[27:50] Right? You need to give it just a couple of paragraphs probably. That depends on how big the LLM is and how capable it is. But also there are, research papers that have
[28:04] demonstrated that the smaller the context you give to an LLM, the better the result. Of course, it has to be small, very accurate, and precise, and contain all the information required to actually generate
[28:18] the answer. So the smaller the chunk or the context, the better. So you get smaller contexts by chunking PDFs. Right? So instead of shelving the whole PDF, you just
[28:33] create a context based on those chunks. So the issue then is how do you generate chunks that are actually meaningful, that are self contained, that makes sense. Right? So, again, there's a lot of
[28:49] strategies, recursive, structural, semantic, agentic, and so on. I think you can categorize them by accuracy and cost. Usually, there
[29:05] are strategies that are very, very, very cost effective. So you can just think of the easiest one is just count a thousand tokens and split the document there, and then you have one
[29:18] chunk and then split again after a thousand tokens more, and then you just continue chunking like that. Right? So they and you can see some issues with that. Right? You may just
[29:30] chunk something just in between the most important part and then you get a very important thing just split into two different chunks. Right? So that would be a shame. And so that's very cost effective, very quick, very, very cheap
[29:46] But probably you're get to get some of those issues. Structural works. It's also very, very cost effective and better than recursive because, basically, it's going to just chunk whenever there is
[30:00] a paragraph change or a new headline or a page. Right? So it's going to use the structure of the content to decide when to generate a chunk and also based on token windows.
[30:14] Semantic is, better one, but then you start adding LLMs to the mix. So it means it's going to be a bit more expensive because you're using GPUs. You're using tokens. You're paying for DLM. Right?
[30:29] And it's not a big LLM. So it's a embedding LLM, actually, so a very cheap one. And it's similar to how you generate vector embeddings for semantic search or vector
[30:42] stores. But, basically, it calculates the embeddings of a chunk and compares or a paragraph and then it generates the vector embeddings for the next paragraph.
[30:56] And then based on the similarity, like, the semantic similarity between both it decides if, like, they're, very similar. They it keeps them both in the same, chunk. But if they differ a lot, then it will decide to
[31:14] chunk them in between. Right? So based on semantic similarity, it will just chunk your data, which is really, really, really cool, very
[31:26] very well balanced, not very like, brute force oriented and also not very expensive to run because it's a very cheap LLM.
[31:39] On the other hand, you can do, like, go full agentic and let a very big and expensive LLM decide how to chunk your data. Right? And probably in the future with even bigger and better LLMs, agentic will
[31:55] be very good actually to do this. But it also depends on how much you are paying for that. Right? There is also some papers already about not chunking at all and just relying on the LLM to
[32:14] read the whole document, but, of course, there is a limit. But it will then, on the fly, decide what chunk to extract to use it for generating the answer. So, basically
[32:29] do you do not chunk during extraction, but you chunk, when you are doing the rag. But, again, this is very new, also probably very expensive. And, usually, for now, I would suggest you just chunk your data, in this extraction
[32:47] step. Then embedding is, yeah, just generate the vector embeddings of each chunk at least. In this case, at the moment, we have only chunked. But then if you do entity and relationship extraction, which is
[33:04] generating the nodes and relationships for your knowledge graph probably, you also want to embed some of those entities. Right? So now here you can embed chunks and you can embed entities. So moving back to one of the diagrams
[33:21] here. Right? Actually, the blue notes are the ones that are, like, part of the vector store. So in this case I would I would embed the review. I would embed the product probably based on the
[33:36] product description, and I would embed the category. This means that and here as well, company concept and chunk. This means that you can access this graph, by doing a vector search
[33:51] to reach one of the blue notes. Right? So here, for example, you can find you can do a vector search to find, specific topic or concept that was mentioned in one of those reviews
[34:06] and then you can do a graph query to get, the products that are related to to the reviews that mentioned that specific topic. So imagine someone is reviewing your products
[34:18] because they have a very specific issue. Let's say it's not compatible with macOS or something. So you can use vector search to find all the reviews that are mentioning compatibility issues, and then you can do a graph query
[34:32] to get the products related to those reviews. Then since you can do multi hop graph queries, then you can also go through the orders and then see if the order dates
[34:46] are on the same month. And then you can see, okay. Yeah. Yeah. People are all those complaints about compatibility issues are actually from this month's orders because we shipped something that's not
[34:58] wasn't fully tested yet, for example. Right? So that shows you, starting doing starting from vector search into a multi hop graph query into single query.
[35:14] Okay. Moving forward, we reach transformation. So now we finished extraction. We have entities. We have relationships. We have embeddings, chunks. We have everything in the database. But now, basically, we just take a step back
[35:31] make a pass, and, clean the data, basically. So here is where we have a chance to find duplicates to ontology alignment and inference and enrichment. So, basically, deduplication
[35:47] and ontology alignment are very similar. Basically means that if, first, you want to find things that are duplicates, so Arnold and Schwarzenegger are the same person, but they are just
[35:59] stored as different entities in the graph. So you want to merge them so that the governor of California is also a star of predator. And so if you ask this to your chatbot, it will agree.
[36:15] But if you don't merge Arnold and Schwarzenegger it's going if you ask your chatbot, your chatbot is going to say, no. There's different people. One is Arnold, and the other one is Schwarzenegger.
[36:28] Probably the LLM with its parametric memory already knows that it's the same person. So it's that's not going to happen. But as an example, you get the point. Right? And ontology alignment is basically
[36:42] making sure that the entities and relationships that were inferred and extracted from your documents make sense and are aligned to your schema. Right? So that, you have
[36:55] you have places, you have people, you have movies, you have companies and everything fits into that ontology. And you don't have animals, for example, here.
[37:08] And if animals are not part of your ontology, then you have no chance to see what to do with that. Maybe you just want to ignore that or review, why was an animal mentioned. Right?
[37:21] Just as an example. And also the relationships. Right? You may have, like, a preset or predefined list of relationships you want to have, like capital off, governor off, star off.
[37:36] But sometimes the LLM will just infer a relationship that maybe you don't want to store or you don't care about, and then this is the point where you can, like, decide, like, should I include this
[37:49] or is it an error, or should I just ignore that? Basically, the transformation step is a time during the process to make sure you clean everything up. And not only clean, but also enrich. Right?
[38:06] Sometimes, you want to add more information to the notes like in LightRAG. If somebody knows about LightRAG.
[38:19] I'm, going to give a bad example first. Right? So when you, generate a, knowledge graph like this, you get a chance now to infer things. Right? So you could infer
[38:32] for example, as a summary of the movie predator. And when you insert this note in the graph, you can also insert a summary, which is generated by the LLM. Right?
[38:45] So that may help you. Right? In the future, if you create a query maybe the summary will be embedded so you can use the embedded summary as a way to do vector search and then start your graph query from there.
[39:01] Right? So that sounds pretty good. Right? The issue is that sometimes if you are generating summaries, for example, those can include hallucinations.
[39:13] Right? So you are storing in your knowledge graph things that may be hallucinated and, eventually, your chatbot may get that hallucination and use that hallucination to answer, a question. Right? So you want to avoid that.
[39:30] I mentioned light. That's a paper that was pretty popular. I'm not sure. Maybe a year ago. They do a little bit of enrichment and they generate summaries and
[39:46] keywords and concepts and build a graph around that. But, basically, what they do instead of using, those inferred attributes as part of the knowledge that is going to be sent
[40:02] to the other, they only use those inferred properties to navigate the graph. So for example, as I mentioned, if you, infer a summary of the movie Predator
[40:15] you use that as an entry point with vector search into your graph, and then you do graph queries, multi hop queries from there. That's great because you're going to find relationships and notes and chunks probably that are going to
[40:31] generate the context for the LLM. But the summary is not actually going to be passed down to the LLM. So even if the summary had an hallucination
[40:43] it may help you just reach the graph and to a hybrid search, but you're not given the summary back to the LLM. So the hallucination will just tie there and not be passed as a
[40:59] context. And then the last step is loading, which is the fun part because we get to insert data into the database. When you generate when you insert
[41:13] knowledge graphs in general, usually, the term is triplets. So you see that in this code. And, basically, a triplet is
[41:27] a, list of three things, which is a node, relationship and another node. Right? So here, in SurrealDB, nodes have IDs like any other record. So we have a record ID for the first node, then the
[41:42] name of the relationship, and the second node. For example, this would be review ID, reviews product ID.
[41:55] And this is code, but it's I think it's almost production code any anyway. And here you can see that you are storing notes, and then you insert and embed those notes, and then insert the relationship that
[42:12] ties both notes together. Here, you can see that I am using a function that takes the note and is going to generate the embedding vector and then insert the note with the embedding vector. So this is
[42:30] a nice utility function that does a lot by itself. And here you can see if I am inserting a node that is not meant to be vector embedded, it's just going to insert a node as it is.
[42:46] This is assuming that you have in your knowledge graph notes that you want to embed, but not all of those notes. For example, you may want to embed products using their product description, but and they are related to an order
[43:01] but you don't want to embed orders. They're just transactional data. Cool. So let's see if there's any other question.
[43:13] I think we're good. And, yeah, let's continue. So now more in-depth in practice.

## [43:23] Demo: exploring a KG in Surrealist
[43:24] This is an example of how a knowledge graph, very simple knowledge graph, can look like in. This is a screenshot from our, GUI, the Surrealist GUI as in graphical user interface.
[43:38] So you can download a Surrealist and, use it to see your database schema, explore your records, run queries
[43:52] create cloud instances, and so on. So here, you can see some things. You have dashed borders. That means I am running in schema less
[44:04] which means that I can add any data to the table, like, MongoDB, for example and not only to the specific columns that I have predefined.
[44:17] And then you can see also dashed lines, which mean record references record links. For example, here, the queue has a reference to a
[44:30] document. So this is this dashed line. Right? While the solid lines mean, proper graph relationships. Right? So here, for example, you see this chunk is connected to concept
[44:43] through the mentions concept relationship. Right? So relationships are actually tables in the database with an in and an out. You can actually also add more properties of metadata
[44:57] or to the relationships themselves. Let's go to the next. Here we go. This is just a quick demo video
[45:13] just to show you around Surrealist. It has this graph visualization page, where you can toggle tables. You can zoom in. You can right click. Click on inspect. Here, you can see that this specific
[45:26] node has the embeddings. So this is showing the multimodal feature of SurrealDB. And that's one of the queries. These are some util
[45:39] queries I usually use. So, basically, they allow me to see what my process ETL what my current ETL process looks like so I can see how many pending chunks
[45:52] are there and the concepts that have are being inferred and so on. This is another query that allows me to see I think this one is to see to find concepts that are, linked to more than one chunk or one
[46:10] document. Because during the process, I wanted to see if if does it make sense to infer the concepts the way I'm inferring it? So I wanted to see if concepts are actually related to more than one
[46:24] chunk. Right? Because if you only have concepts that are related to one chunk, then basically there's no no benefit of inferring those concepts. Right? But if you have concepts that
[46:36] that are related to a lot of chunks, then it means that the concept is like a real concept that's part of your domain and will help the right work.

## [46:49] Agentic RAG & tool calling
[46:49] So now navigating the graph navigate navigating the graph, there are two ways. The traditional rank way, which is where you have a user sending a prompt
[47:05] let's say, to a chatbot agent, and then it will retrieve data from the database. And then let's say you get five chunks with very high score, and then
[47:18] those three chunks are going to be passed to the LLM as context. And then the LLM will use your prompt that context to generate an answer. Let's say, about, yeah, our
[47:32] customer support question about troubleshooting or something. This is traditional RAG. Right? Again, a little bit simplified. Now we have a agentic RAG that looks like this.
[47:49] If you are familiar with modern LLMs, you know that they can use tools. Right? So Claude, OpenAI most of the providers, you will see in their models that they are
[48:04] have this special feature of calling tools or calling functions. Basically, that allows an LLM to decide to use web search or to decide to use an MCP.
[48:20] And, in this case, this is a multi agent RAG system. So let's say the system is the whole chatbot application, and it gets a prompt. So there will be a couple of agents doing different things.
[48:36] So let's assume you have an agent that works as a router. So it will get the prompt, and the agent will figure out, I guess, this customer service request or is this, like, a should I route this to
[48:53] a different department? Or is this about, mouse and accessories? Or is this about software? Right? So you can have an agent that takes those decisions.
[49:06] You can have then other agents that now based on your domain, they will basically query the knowledge graph to then generate the right context. So as you can see, web search is a very common built in tool that LLMs have.
[49:24] Sometimes you don't have to provide the web search web search tool that's just already embedded in the in the model. MCPs are very common, and those you need to connect to your agent in a way
[49:41] depending on the framework you're using, if it's LangChain, Camel, or. And another way, is, yeah, to create your very custom tools, or in this case, this would be like a tool set
[49:57] for SurrealDB knowledge graph. And within that tool set, you have you can have very specific tools, like a tool that it's, like precreated to do hybrid search by topic or do
[50:11] a monthly bestseller review. Right? So depending on your use case, you may have very custom specific tools, but, also, you can have, a very
[50:24] like, open ended tool and allow even the LLM agent to write this SurrealQL query that is going to be sent directly to the graph.

## [50:38] One query: vector + graph in SurrealQL
[50:38] And here it is. So this is the one example query where you can see both vector and graph happening, which is maybe it looks scary, but it's not really that scary when you compare
[50:55] this with the alternative, which would be to have a vector query going to a vector store in one database and then get the results. So, basically, you have now a query language and your Python code. And then with the
[51:11] results, you again need to do something with that and do a graph query to another database. So there's a lot of glue code that you need to add in between
[51:23] and then manage different database instances and so on. While with a single query, you get, everything, from one place. So here you can see that, if you're familiar with SurrealDB, you will notice
[51:39] this line 84 is the vector search one. For those not familiar with SurrealDB, this is you can see this is not SQL. This is similar to SQL. We call it surSurrealQL.
[51:55] And this is the notation for vector search. So you're doing here, basically if you have an embedding vector coming as a parameter, as a as an argument
[52:07] to your query this coming from vector embeddings model basically, it's asking for the top five. So here five is the k value
[52:19] and with an effort of 40. Right? So the higher the effort the more accurate but slower it will be. 40 is a good balance. Sometimes if you don't need that much accuracy or a full list of all of
[52:37] the neighbors that you are optimizing for latency, you can set this up to 17, for example. That's super fast. And depending on on your chunks, you may get already the ones you're expecting to get.
[52:53] So here, basically, this inside select is going to find the chunks that are similar to your prompt. And then that is used by the outer select, which is going to relate
[53:09] those chunks to their original documents so that in the result of the select, you do similarity search against the chunks, but the result you actually get is the document. So you know what which document is the reference.
[53:25] Then you can also limit by a threshold. So you don't want scores below 60%, for example to make sure that whatever you're generating and given the to the LLMs context
[53:39] have high scores. And then the outermost select here, you can see an array transpose, which is basically just rearranging the results I get from this select into a nicer form. So, basically, I'm creating
[53:55] here a JSON object that contains contents, scores, chunks and the chunk indices. So here you can see the result. It's basically a list of chunks, where I have the highest score.
[54:11] And, basically, this is representing a single document. So it should be below if I scroll down. And we think I get all the chunks, grouped because I only care about their the document because I want to use
[54:27] the document as a reference in the answer. But here you can see the chunk that was, that had the highest scores maybe was this commencement information. So here you can see it's a good example of hybrid query
[54:42] vector search with a very simple graph query but also you are, like, rearranging the results. And this is how you provide this as a tool.
[54:55] In this case, I am using. So I created a retrieve tool, which is just going to take a search query and use that to run a query like this. So, basically, by using this decorator, this retrieved
[55:14] tool is being registered as a tool to my original agent. And using the docstrings, the agent will know when to pick this tool. So whenever it wants to retrieve documents from the knowledge
[55:26] graph, it will know to call this tool. And it will know that, the only argument is the search query which is super straightforward. And, yep, the code is very simple. Basically
[55:40] it's just going to embed the query. And this embedding here, the result of the embedding model is what gets passed in line 84.
[55:53] And then the results are just concatenated and sent to the LLM to generate the answer. So, basically, here, the LLM will have the name of the document. So it will use the contents of the chunks to generate the answer, but
[56:08] also, it will be able to give to say to the user which document was the source for giving the answer.
[56:22] And in the okay. This is also a good example. This SurrealQL, this is a tool that has like, hard coded query. Right? So the query
[56:34] is in the code. The only thing that's not hard coded is the embedding and, optionally, a threshold. So it means that it will run this query every time whenever the retrieve call is called. But you can also have the LLM generate the
[56:51] SurrealQL. Right? So this query doesn't have to be hardcoded. The LLM can just write its own query, for very dynamic questions, for example. In that case, of course, the LLM may
[57:08] hallucinate a little bit and generate queries that don't work but it's all about the system prompt and how you optimize the system prompts. If you're going that route, I suggest you create some
[57:23] a few shot examples. So give the LLM examples of queries similar to the ones you expect it to generate. And based on those examples you give, the LLM will more accurately generate queries.
[57:38] I think we're reaching the end of the time we have got today. So let's see. I think there's no more questions in the chat. This is the last chance for you to ask anything else.
[57:55] Here you can see an example run. This is the agent that has already my tools registered, and here you see the system not the system prompt, but the instructions I am telling use the knowledge base to generate your answers and
[58:10] mention the document in the answer because I'm assuming the user wants to have the document ID. This is outdated as you can see. It's actually supposed to print out the file name
[58:23] which is useful for the user, not the ID. Cool.

## [58:31] Wrap-up
[58:31] Thank you everyone for joining. Hopefully, it was not too technical not too high level for you. I think it was a good mix. Hopefully, you had a good time. Make sure to, yeah, subscribe to the newsletter.
[58:48] This is going to be published in the in our blog. So it will be have a longer format with all references links to articles, frameworks, libraries. I used to do the parsing, the chunking.
[59:05] So that's very, very helpful. And, yeah, hopeful hopefully you will join the next time, and we'll continue work talking about.
