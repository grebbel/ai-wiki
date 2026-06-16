---
title: 'Stanford CS224W: Machine Learning w/ Graphs I 2023 I Knowledge Graph Embeddings'
video_id: isI_TUMoP60
url: https://www.youtube.com/watch?v=isI_TUMoP60
channel: Stanford Online
channel_id: UCBa5G_ESCn8Yd4vw5U-gIcg
channel_url: https://www.youtube.com/channel/UCBa5G_ESCn8Yd4vw5U-gIcg
publish_date: '2023-12-07T10:19:14-08:00'
upload_date: '2023-12-07T10:19:14-08:00'
category: Education
duration: '1:10:04'
length_seconds: 4204
view_count: 13927
is_live: false
thumbnail: https://i.ytimg.com/vi/isI_TUMoP60/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGFQgWyhlMA8=&rs=AOn4CLBOuDwt7E4TjFqry2Qg36CWjX5lsQ
caption_tracks:
- language_code: en
  name: English (auto-generated)
  kind: asr
  is_translatable: true
- language_code: en-US
  name: English (United States)
  kind: manual
  is_translatable: true
description: "To follow along with the course, visit the course website: \nhttps://snap.stanford.edu/class/cs224w-2023/\n\nJure Leskovec\nProfessor of Computer Science at Stanford University\nhttps://profiles.stanford.edu/jure-leskovec\n\nLearn more and enroll:\nGraduate Course: https://online.stanford.edu/courses/cs224w-machine-learning-graphs\nProfessional Course: https://online.stanford.edu/courses/xcs224w-machine-learning-graphs\n\nTo view all online courses and programs offered by Stanford, visit: http://online.stanford.edu"
notes: |-
  Transcript fetched via youtube-transcript-api fallback after the Playwright path hit 'transcript panel did not render' timeout (GH #2). Video has TWO caption tracks: manual (kind=manual) and ASR (kind=asr); picked the MANUAL track for highest fidelity. Light cleanup: dropped [music]/[applause]/[beeping] non-speech markers, grouped consecutive segments into ~12-second windows with [mm:ss] timestamps, speaker-turn breaks (manual track preserves speaker labels in caps). 1247 raw segments -> N grouped windows (replace N after run).
---

## Transcript
[0:05] Hi, everyone. Welcome to the class. Jiaxuan covered the topics around graph neural networks over the last few weeks. But now, I'm and I'm going to cover
[0:20] for some of the next topics. So here is what we'll talk today about without any bugs. We so far talked about graph neural networks and how to handle graphs with a single type of relation.
[0:34] And then, in the last lecture, we then talked about heterogeneous graphs and how do you build GNNs for heterogeneous graphs. We talked about the relational GCN, the knowledge graph--
[0:47] we talked about the relational GCN in the last graph-- in the last lecture. What are we going to do today? We are going to talk about knowledge graphs, which are these directed graphs with different relation types that usually have no features on nodes of the network.
[1:04] What we are going to talk to today about is an analog of Node2Vec and DeepWalk that this shallow embeddings that we talked about at the beginning of the class, and generalize that
[1:19] to heterogeneous graphs. That's one way to think of this. The task we'll be talking about is the embeddings for knowledge graph completion. That's the way to think of this. Last time. Sorry, sorry, sorry.
[1:33] So last time, we talked about heterogeneous graphs, we talked about graphs with different node types and different relation types. Yes. Ignore everything I've said so far.
[1:45] Sorry. Sorry. It was the wrong slides. That's why it was in October, that's all everything is wrong. Sorry, sorry, sorry. Brand new lecture. Breath in. Look, you guys are the best, you arrived late.
[2:00] You won't be confused. So if you are confused, ask them. So brand new lecture, start from scratch, ignore everything I said. Really sorry. Going again. So these are the announcements that are good, read them.
[2:14] They've been verified. This is the CS224W machine learning with graphs. Today, we are going to talk about knowledge graphs embeddings. So the topic is right. What did we talked about last time?
[2:28] We talked about how do we generalize graph neural networks to heterogeneous graphs, where we have edges of different types and we have nodes, potentially of different types.
[2:40] We talked about relational GCN where we learn a graph from-- basically, we learn from a graph with multiple relation types, and we use different neural network weights for different relation types.
[2:52] So we basically took the GNN architecture, but generalized it now so that this message-passing functions are relation-specific so that we have more expressive power when working with heterogeneous graphs.
[3:07] Today, we are going to take this and further generalize it to the notion of knowledge graphs. Let me first tell you what is a knowledge graph and why is it so important and why is it so useful.
[3:20] So knowledge graphs allow you to capture in a graph form, in a relational form knowledge about entities and their relations. So we are going to capture entities, types, and the relationships between them.
[3:34] You can think of nodes as entities. And node types are-- and these nodes are labeled with their types. And then edges between two nodes capture the relationship between the entities.
[3:48] Knowledge graph is an example of a heterogeneous graph. But the reason why we call these things knowledge graphs because the idea is that we encode our knowledge about a given domain in this type of graphical form. So we can think of this as a knowledge base
[4:02] over which you can reason, over which you can retrieve, and allows you to bring in the knowledge to your machine learning model. So that's the idea. What would be one example of a knowledge graph?
[4:15] For example, if you are answering questions, predictions about academia and papers, then, for example, a bibliographic network, you can think of it as a knowledge graph. You have conferences, papers, titles, year of publications,
[4:30] and authors, and papers have citations to each other. So this is like a schema of this heterogeneous knowledge graph with five different node types and five different relation types.
[4:42] Now, I'm basically encoding all I know about all the publications ever published. Another example, especially that is extremely useful, is biomedicine, where, again, you
[4:56] have a lot of different entities, from drugs to diseases, adverse events, proteins, pathways, and you want to encode this knowledge in a graphical form. Here, we have different types of relations,
[5:10] like is_a so hierarchical associations between different things, treatment that are given drug treats for a given disease, a drug may cause adverse side effect of migraine in this case.
[5:24] You can build this knowledge graph scaffold that you can use as a knowledge base over which you can then reason or over which you can then learn. And there's many other knowledge graphs
[5:37] that I'm going to show you later. For example, Google answers a knowledge graph when you type questions into the Google search box. Same with Amazon. Amazon has a knowledge graph of all their products,
[5:50] their properties, sellers, and all that is, in some sense, their knowledge base. Facebook calls this the Facebook Graph API, if you want to access Facebook as a graph. If you look at Facebook, in a sense,
[6:04] it's not only people and their relationships, but also what schools people went, what locations they attended. That's all nodes in this knowledge graph. It's all resolved to the level of entities.
[6:19] There are other examples of these technologies. From IBM Watson to Microsoft has its own, they call it Satori, LinkedIn, Yandex, and so on and so forth.
[6:32] Just give you one example of the application is for serving information. When you ask, let's say, here, Bing, what are the latest films by the director of Titanic? They actually parse this go to the knowledge graph,
[6:51] find the director, and then look at what is this director linked by the relation that they directed, what movies they directed. And that's how they retrieve. Usually, if you think about question answering,
[7:07] let's say, systems. If you think of Siri, if you think of Alexa, they are powered by the structured knowledge in the background. Siri uses a humongous knowledge graph of the world's knowledge
[7:19] that when you ask it a question, the thing queries and gives you the answer. Here, I'm showing you an example of a architecture of this conversational question-answering system,
[7:34] where the natural language understanding is only a part of this. And in particular, what the key part is to take this language parse it into a set of candidates
[7:49] that you are then retrieving from the knowledge graphs, and then returning back to the user. So that's the key in this case. Today, we are going to talk about this knowledge graphs.
[8:02] And if you think about general knowledge, knowledge graphs, then FreeBase, Wikidata, Dbpedia are examples of this. You can take an entire Wikipedia and you can represent it as a graph of nodes and their properties
[8:18] and relations between them. FreeBase is another example of this. This was, I think, a project that Google acquired a couple of years ago for a lot. I think the price was in billions.
[8:31] What is common characteristics to these things is that they are massive, they have millions of nodes, millions of different edges and relations, and they are really incomplete, in a sense that knowledge
[8:44] has not been completely mapped in this knowledge graphs. Usually, the reason, there is two ways. One is we haven't entered all the knowledge in, and the second reason is we haven't yet discovered all the knowledge.
[8:58] If you think about biomedicine, biomedical knowledge graphs are incomplete because we don't understand fully the, let's say, human biology. So clearly, there is information we are missing because we haven't discovered it yet,
[9:10] versus a knowledge graph like FreeBase, I'll show you later. 83% of people that appear in freebase as nodes don't have a year of birth, I think, is the statistic, because nobody added that information in yet.
[9:25] Given what we'll be talking today about-- given a massive knowledge graph enumerating all possible facts becomes intractable. But what we would like to do is, the question is,
[9:38] can we predict plausible but missing links in this knowledge graph? So can we somehow embed nodes in the knowledge graph? To show you, I said earlier, a prominent example of knowledge graphs is FreeBase.
[9:52] This encodes knowledge about this commonly known entities that appear in the world. It's about 80 million entities, 38,000 different relation
[10:06] types. So there is 38,000 different edge types and 3 billion edges. Because by the relation-- so the point is it's not five relation types,
[10:19] it's 83,000 different relation types. So the world knowledge in this structured forum is very complex. As I said, 93% of people that appear in FreeBase
[10:35] don't have a place of birth, and 80% don't have a nationality. So there is no link relationship of that person nationality and to the, let's say, country or nation mapped explicitly
[10:50] in this knowledge graph. Yes. I guess, when you're recording data in these knowledge graphs, is it preferable to have a proliferation of relation types, like lots of relation types,
[11:02] or is it more useful to have grouping of relation types from a learning perspective? Good point. So what you are asking is to say you have-- here, I emphasized, you have this huge number of relation types. And the question is, is that too much?
[11:17] What should you do? I would say there is an entire, how to say, industry, or an entire field of how do you build ontologies, how do you build this knowledge bases.
[11:31] And it becomes very, very tricky how do you bring any structure to this 38,000 different relationships. Usually, what would happen is that you would have them in some hierarchy, if possible, where these relationships would
[11:45] get more and more fine grained, but still allows you to reason between different relationship types. That becomes quite important. In terms of publicly available data sets that people like to use, there
[11:58] is this FreeBase 15,000, which is a graph on 50,000 entities, between 200 and 1,300 different relations, and about 300,000 to 600,000 different edges.
[12:12] So if you want to little academic benchmark, this is what NeurIPS papers tend to use. But really, the full data set is up here, very few papers have the guts to use the big data set
[12:27] because it's massive. But that's the idea. Now, what we will-- so now let's-- we talked about this knowledge graph concept. Now, let's talk about what is the knowledge graph completion
[12:40] task that people like to do. A knowledge graph completion task is defined as follows. Given an enormous knowledge graph, the question is, can we complete it? It's almost like a link prediction task,
[12:53] but it's a bit more nuanced. And this link prediction task for knowledge graph says, given a head and a relation type, predict me the missing tails.
[13:05] So it would be for a particular person, for a particular relation type may be born in, give me a list of places where that person might have been born. Because a single person can be born only in one place,
[13:18] I'd only take the top one. But in other cases, maybe it'd be like visited. Tell me all the places that Napoleon visited, then it'd be a ranking and somewhere I would cut that.
[13:31] One example of the task would be, for the predict the tail, you would predict "Science Fiction" for the head entity J.K. Rowling. In the genre relation, the question
[13:46] is, what is the tail of this query? It would be science fiction or it would be, I don't know, youth literature, or however you want to call it. So that's what we would like to be able to do.
[14:00] As I said, it's a bit different than link prediction because I'm given the head and the relation type. Now, as I mentioned in the beginning of the lecture, the way we are going to do this is we are going to learn a shallow embedding of the nodes.
[14:13] So it means that for every node in the knowledge graph, we are going to learn its coordinates in a shallow way. So we will not be using GNNs, but we are moving back to this idea of shallow embeddings, DeepWalks,
[14:26] and Node2Vec. But, as you will see, we will not be using random walks, so we'll just be using shallow embeddings. In terms of knowledge graph representation,
[14:40] the way we think of it is that it's a set of these triples: head, relation, tail. And the idea is that we want to model entities and relations as embeddings or vectors in some Euclidean space.
[14:52] And we want to associate entities and relations with shallow embeddings. As I said, no GNNs. The reason, perhaps, why no GNNs is because this knowledge graphs usually have no node features.
[15:06] Maybe you have a node type, but not more right. All the information is in relations. Then, the idea will be, given a true triple, head, relation, tail, the goal is to find the embedding for the head relation
[15:19] that is close to the embedding of the target. So we'll be talking about embeddings of I will give you a head and I'll give you a relation, you will produce me an embedding of this thing.
[15:33] Hopefully, the embedding of this thing will be close to the embedding of the target. So that the answer to this query is this target. That's the hope. The question then is, how do you embed this thing
[15:47] and how do you define closeness? What is interesting, notice, I'm not embedding just a node, I'm embedding node, comma relation. And I'd like that this embedding node comma relation in the space is close to the answer to this.
[16:03] The correct thing has to be close to where the embedding of this comma relation is. So what we are going to do today is we are going to learn about different methods
[16:16] to produce embeddings of knowledge graphs as well as the relations that are in them. These embeddings will be shallow, so we'll work in the transductive case. We are going to use different geometric, Euclidean geometry
[16:32] type intuitions, and we are going to talk about different types of relationships that our embeddings will be able to capture. We'll talk about four different methods: TransE, TransR,
[16:45] DistMult, and ComplEx. It doesn't matter yet what they are, I'm going to define. It doesn't matter what exactly this means. But basically, we are going then to look at different types of relations. We'll talk about symmetric relations,
[16:58] antisymmetric relations, inverse relations, composite relations, and 1 to n relations. I'm going to explain these and we are going to see how different method is able to embed different types of relations.
[17:12] That's what is going to happen, and the rest of the lecture will go through this table line by line. We are going to fill in this checkmarks and crosses for each of these things.
[17:27] So at the end, basically, this table will be filled in and it will make sense. So the first method I want to talk about is the first line of my table here is the TransE.
[17:43] Are there any questions before we jump in? Yes. I mean, just based on our definition, where we're taking the head, the relation, and then the target is like the thing we're trying to predict.
[17:55] It's like saying that the graph is like directed, because we're always saying there is a direction from graph edge that already gives you directions toward a target. So there's a relation. Yes, you can-- great point. So you are asking, is the graph directed?
[18:07] Yeah, you can think of it that it's directed. But if we are brothers, then I have a link brother to you, but you can also have a link brother to me. Yes, we are talking about directed graphs,
[18:21] but some relations can go both ways as we are going to see. So that will be one of the kind of properties that we are going to talk about. Super. So here is the TransE intuition, and it's really
[18:35] about this translation intuition. Where the idea is for the triple head relation tail, I would like the following in my vector space in my Euclidean space. I'd like h plus r to be equal to t.
[18:51] If the given facts are true and otherwise, I'd like this to be different. That's the intuition. So the way this would look like is to say the embedding of an h comma r is that I take the embedding of h,
[19:05] I have some embedding for r so I move in this direction, and hopefully, I end up close to the target t. I'll have an embedding for every relation, I'll have an embedding for every entity.
[19:18] So if this is a relation brother and if this is me, then, from me to brother, here should be all my brothers. I know, if there is a relation sister, then I'd go this way and here should be embedded all my sisters.
[19:31] Just as an example. Or if there is a relation Uri likes to eat, then I would learn I know something down here, and here would be all the dishes that Uri likes to eat. That's the idea here.
[19:44] So the idea is that, if I have an embedding of Obama, I have an embedding of nationality, so now I say, what is the nationality of Obama? I take this. I take the vector that I learned for nationality.
[19:57] I move in the space. Wherever I land, this is where I want his nationality to be embedded. That will be the objective function. Of course, it won't be spot on, but that's the idea. Basically, this means that we are
[20:10] going to learn embeddings of entities as well as the embeddings of relations or vectors for these relations, with the goal that if I start at the head, I move in the direction of the relation-- that is specified by the relation,
[20:24] I arrive at the target. And for people who have MLP background, remember, when we had this some time ago, there were these word embeddings and people were so fascinated that if you take a King and move in one direction,
[20:38] you move to the Queen. It was consistent for different Kings and Queens of all different world countries, that vector in which you move was the same for them all.
[20:52] Or if you took a name of the country and you look where is the capital embedded, it was the same direction. From China and Beijing, from USA and Washington, DC, for Germany and Berlin, it was all these vectors.
[21:06] So that's the one motivation for this. Here's the algorithm, I throw pseudocode up. But the reason I want to throw it up, like show it here, is that I want to show you that the way you learn this
[21:19] is in using a contrastive or triplet loss. So that's the concept I want to teach you here. So the way we think of this is that, basically, we initialize the embeddings of uniformly
[21:31] at random of entities and relations. And then, what I'm doing is I'm basically-- I need to create negative samples for every triplet in my knowledge graph head relation
[21:46] tail. I say, aha, for a given head and a given relation, the tail is a positive example. But the real tail is a positive example, but now I need to find a negative example tail.
[22:01] Now that I have a head, real tail, and a wrong tail, my goal in the objective function is that the distance between head plus relation to the real tail should be smaller than the distance
[22:14] from the head plus relation and the wrong tail. And then, of course, here, you ask yourself, and this is called a contrastive loss that favors lower distance, higher score for valid triples,
[22:29] and wants to have high distance, lower score for the corrupted ones, for the negative ones. And that's the contrastive loss I want to explain here. Yes, question.
[22:41] Yes. So in the line 10 or [INAUDIBLE] whenever you sample your negative sample, you have h prime as well as t prime. Does that mean you are sampling for both like a real head and a wrong tail?
[22:56] Yeah Good question. You can do it both ways. You could say, for the head relation, I want to get a correct tail and the wrong tail. The question is, what is the wrong tail? If you will pick a random entity,
[23:09] that will be a too easy tail. So what you usually want to do is you want to pick a tail that is of the same type, but wrong. So if I'm going from country capital-- sorry, country capital and the city,
[23:24] then I want the wrong tail to be a different city. I don't want the wrong tail to be a chocolate bar. That won't work, it's too easy. So you want to be kind of careful how you do this negative examples sampling.
[23:37] But this is basically, in some sense, great question. How do we handle transitive relations? If you have a brother, then he's also your brother, but the vector only points in one direction. Great question. So the question is how do we handle transitive relations.
[23:52] Let me get to that. We said we are going to fill in that table. That's exactly the question I want to address next. What is this able to learn and where it's clearly going to fail? Now, what we want to talk about is exactly what
[24:07] the question was about. Relationship in heterogeneous graphs have different properties. Some may be symmetric like a brother or a roommate. I'm your roommate, you are also my roommate,
[24:19] it has to be that way if we are roommates. Some may have inverse relations. If I am your advisor, you are my advisee.
[24:31] It's that way. This means that if one exists, the other one should also exist. So we can categorize this type of relationship patterns and ask our knowledge graph embedding method,
[24:45] like a TransE, is it able expressive enough to capture this type of patterns? Now, what patterns of relations are we interested in? And here are the four I'll talk about.
[24:58] First one is symmetric or antisymmetric relations that says if head and tail are related by relationship r, and then tail and head should also
[25:10] be related by relationship r. So this is like, if I'm your brother, you are my brother as well. Antisymmetric means, if h is related to t, then t cannot be related by h using the same relation.
[25:26] Then you have inverse relations, which would mean that this is like advisor-advisee type, where whenever h is an advisor of t, then t is an advisee of h.
[25:39] That's what we say an inverse relation. Then we have composition or transitive relations, where you say, if x and y are related by r1 and y and z are related by r2, then x and z should be related by r3.
[25:56] If you think of this, it's like if I'm someone's son and that person is someone else's daughter, then that person is either my grandmother or something
[26:10] like that. I think I didn't see it well, but you see what I mean. It's like based on relationship, the third one is determined. That's what we say composition of relationships or transitive relations.
[26:22] And then the last one is this 1-to-N relations, where you can have a case where the same head is in relation with many different tails. So it could be a case that I can have more than--
[26:37] I can have more than one brother so there could be many tails that satisfy this relation. Yes. This composition assume one order for operations because your husband's mother won't
[26:49] be the same as your mother's husband. No, this assumes order. This assumes order. So let's now look what TransE allows me to do.
[27:01] Is it able to give me to model antisymmetric relations like hypernym type relations? It can allow me-- it allows me to do that. If h is in relation with t, then t cannot be in the same
[27:18] relation with r. So this is what this allows me to do. It also allows me to model inverse relations, by basically
[27:31] saying, if h is related to t, then t can be related to h according to this other relation. It's just a vector pointing in the opposite direction. So that I can also do.
[27:44] I can also do composition by saying, if I can go from x to y by r1 and from y to z by r2, then I can also learn a relation that goes directly
[27:56] from one to the other. So these things are naturally composable. This is in terms-- my mother's husband is my father or something like that.
[28:12] This is what we can model. But here's an example of a relation that TransE is not able to learn, like a symmetric relation, like family, roommate, brother,
[28:25] and so on. Then, I cannot model symmetric relations, the only way to model them is to embed h and t to the same spot and have r equal to zero, then h plus r equals t and t plus r
[28:41] equals h. That's the only way this would be possible. So we say that you cannot model symmetric relations with TransE. So that's one issue.
[28:56] And then another issue is that TransE can also not model 1-to-N relations when it's one to many relations. Because the only way to model one to many would be that,
[29:09] again, t1 and t2 have to be embedded at the same dot-- at the same spot. So there is no distinction between these two entities. You only move in one direction and you cannot do this
[29:24] because t1 and t2 will be mapped into the same vector, even though they are different entities. These are the reasons what TransE can do and what TransE
[29:38] cannot do. Based on these intuitions failures of TransE, I'll now show you a different method that people have invented that will allow
[29:52] us to fix some of these issues. So now we completed the first line of that table and we are now moving to the second line of the table, which is the approach that is called TransR.
[30:09] The way TransE models translation of any relation in the same embedding space. The question is, can we design a new space for each relation and do the translation in the relationship-specific space?
[30:24] That's what TransR tries to do. TransR is going to model entities as vectors in the entity space, but model each relation as a vector in the relation space, where
[30:42] r will be k dimensional. We will actually going to have then a matrix that is going to map from this k dimensional space
[30:56] back into the d dimensional space in which the entities are embedded. So we are going to have this projection matrix. That's the idea for TransR.
[31:08] TransR are models entities as vectors in the entity space that is d dimensional and models each relation as a vector in the relation space with m sub r being this projection matrix that is relation-specific.
[31:25] So the scoring function, so the way we are going to measure the distance between head and tail for a given relationship r is the following.
[31:39] We are going to apply a relation-specific projection to the entity h, that's why I have it here. We are going to apply the same projection to the entity t,
[31:55] and then we are going to move according to the vector r. Here, basically, for every relation, we are allowed to linearly more of the space in a relation
[32:12] specific way. The idea is that, maybe the entities in the original space are embedded this way, but then our projection matrix is going to embed them differently. And then the relation embedding vector
[32:26] will tell me how to move from head to the tail. That's the idea. Here, I'm learning three things. I'm learning the embeddings of entities, I'm learning the relation vector r,
[32:41] and I'm learning the projection matrix for every relation. That's the idea. Now, let's reason about what this is going. And just maybe in terms of how do I learn this,
[32:55] I basically use-- this is my objective function. It's analogous to the TransE one, where we had the same, we said the distance between h plus r and t has to be small.
[33:10] But in this case, in this case, I'm using this projection matrix. So it's essentially the same objective function that I'm trying to optimize, just that I add a matrix M as part of the learning as well.
[33:27] Now, what is interesting is that, in this case, I may actually be able to model symmetric relationships because TransR will allow me to do this because the matrix
[33:41] M will allow me to map from the two entities, from the space of entities to the same spot in the relation specific space.
[33:55] So this means that we can map h and t to the same location in the space of relation r, and h and t are still different entities in the original space.
[34:08] So I can learn this type of mapping, and I will be able to handle symmetric relations, something that TransE was not able to do. I am also able to handle antisymmetric relations.
[34:25] This is actually the same as in the TransE can do, where I can learn a projection that will keep the entities apart, so I won't
[34:37] be able to come back to it. So that's the same as what TransE was able to do. Now, how about 1 to N relations. One to many relations means that one entity
[34:51] is related to many other entities according to the same relation. Again, TransR will be able to do this because we can learn this projection matrix so
[35:05] that different targets, different tails get mapped to the same point. So the idea is, if in my original space I'll have h, t1 and t2, it's possible
[35:18] to learn a projection matrix that maps both of them to the same point. So in this relation space, now I said aha from h according to r, there's multiple entities here. Even though in the original space
[35:31] for some other relationship, I'm still able to distinguish these entities. Yes. Can you make a generalized claim that if an embedding method can handle symmetric relations, then it can handle 1-to-N relations?
[35:46] So the question was, can you make a general claim that if a method can handle symmetric-- sorry, symmetric relations, then it can handle one to many relations.
[35:58] I don't think so. My answer would be no. But for a proof, maybe we can talk after the-- Good. Thank you for the question.
[36:11] Yes. Why do we use just a linear transformation from the entity space to the relation? Why don't we do like an MLP or something? Good question. So the question is, why are we using a linear transformation? Why wouldn't we do a nonlinear transformation?
[36:36] I guess you could. I mean, I think you would learn an MLP that would basically take these coordinates and learn how to transform them.
[36:48] I'm trying to come up with a reason why that would be a bad idea. It's a good question. My sense, does anyone see why this would be a bad idea?
[37:01] Competition expensive you mean? Yeah, I don't know. We could see whether this is possible to learn now you are learning one separate MLP. It will be a very complicated learning loop
[37:15] because you will learn the embeddings of entities, then you will want to learn the MLP, you will want to learn the r. So it's a good question whether this will work in practice.
[37:27] But if somebody gives you an MLP that works and the embeddings, there's no problem with that. Good question. It'd be fun to try. Cool.
[37:39] So this is one to many. And then in terms of inverse relations, again, this is easy to see because TransR is just a generalization of TransE.
[37:51] So if the projection matrix is for two relations, two inverse relations is the same, then, basically, one relation vector is an inverse of the other relation vector.
[38:04] And you get this the same way we got it in TransE. And then, the last thing to discuss is this composition of relations. And the way, perhaps, to see this
[38:19] is that I'll give you some visual proof for high-level intuition why this is possible. And the idea is that TransR models a triple with linear functions, which are chainable.
[38:32] Linear functions are composable, so everything will work. That's the high-level intuition. Here, I have a longer proof that maybe in the interest of time
[38:47] that I spent at the beginning talking about last year's lecture that was slightly different, I will skip. But the way you can do this is, first, you need to define this kernel space of a matrix.
[39:02] And then you can say, what is composition of relations if x and y are related with r1 and y and z by r2, then I want to show that y and z according to r3
[39:16] is possible. And basically, you start writing it out according to our linear algebra with this projection matrices. And then that will--
[39:28] and then you can basically define or come up with the answer that, because these matrices are linear operators, you can chain them and get the correct answer at the end.
[39:41] Yes. [INAUDIBLE] vector spaces, like the space of entities and the space of relations. And all these rules are examining injective, subjective, or bijective.
[39:54] Can you view it that way? Can you ask again? If it's too-- so basically, the space of entities is Rt, the space of relations is Rk, so it's just two vector spaces.
[40:09] Correct. So therefore, we're looking at composition of linear maps. Exactly. It's a composition of linear maps across these two vector spaces. So then, if it's 1-to-N, that would be looking at if something is subjective,
[40:23] then we can think about injective or if it's bijective. Correct. That's maybe another way to say it is that, basically, you have two vector spaces, one is a d-dimensional, and I think the other one we said is a k-dimensional.
[40:36] You are basically learning at looking at compositions across these two, and you are looking at this, as you said, bijective, subjective, or injective relationships across the space. So that be related to the earlier two questions
[40:50] about what earlier our friend asked. If it's 1-to-N but it also be symmetric, that would mean, just because it's subjective, it doesn't mean it could be bijective. Exactly.
[41:02] Well, that answer this question as well about the MLP because we're looking at linear composition maps between, therefore, you can't use them all. Exactly. That's a great point. Actually, I was thinking of exactly the same.
[41:16] Great observation, actually. So when your MLP would break is here. You would lose composition of relations with the MLP. So that's the place it could break.
[41:31] Great part. Exactly. Exactly. Cool. Good. I continue. So this was our second method that's called TransR and defines these two vector spaces
[41:45] and maps these projection matrices from one to the other. What I want to do next is talk about the third method in this space called this DistMult.
[42:03] The idea behind this notion of bilinear modeling. So far, our scoring function was just Euclidean distance or it was an L2 or L2 distance between the embedding
[42:17] of the hat comma relation and the embedding of the target and we wanted to minimize that distance. Another line of work that is a bit different is trying to adopt what is called bilinear modeling.
[42:32] In DistMult, entities and relations are using vectors in Rk, but the scoring function that measures the distance between the head and tail
[42:44] according to the relation R will have the following form, where you are going to basically go over the individual coordinates of h, r, and t, multiply them together, and sum them up.
[42:58] So the way you can think of this is that, basically, you have the head, you have a relation-- you have a head and a tail, you have a relation, you multiply these things together, coordinate-wise,
[43:12] and sum them up, and that is your score. So now, we defined the different scoring function. And we are still going to have a head relation and a tail embedding as we had it
[43:25] in TransE, just the scoring function is now different. The intuition for the scoring function is that it can be viewed as a cosine similarity between h
[43:39] times r and t, where, in our case, h times r would be defined as a summation of h sub i and r sub
[43:53] i. So the idea would be that, basically, if you have your target t2 and you have your target t1,
[44:06] then you can basically think of this vector h times r. And when you multiply it with t, that's
[44:19] basically coordinate-wise multiplication and a summation. So that's the way to think of this.
[44:33] Let's now look at what DistMult allows you to do. So let's first look at one to many relations. So here, I have head, relation, tail 1, head, relation, tail 2.
[44:49] Can DistMult model this? It basically can because it can put a tail 1 and tail 2 in such a way that basically the cosine distance
[45:05] between these vectors will be equal. So that's the first thing.
[45:17] The second thing is to go and ask about symmetric relations. Here, this is, again, this brother type relation. The way DistMult can naturally do
[45:33] this is because, basically, our scoring function is the same regardless of head and tail. So basically, multiplication is the order
[45:49] in which I multiply numbers. It doesn't matter. So I'll get the same score if I'm scoring head, relation, t, or if I'm scoring tail, relation, head. So I will naturally get that.
[46:02] Of course, because I get this property, I then cannot get the antisymmetric property because DistMult cannot model antisymmetric relations. Because the score of head, relation,
[46:15] tail is the same as score of tail, relation, head. This means the score of head and tail and the score of tail and relation
[46:30] will always be the same. So you cannot distinguish the two. So you cannot say, if head is in relation with tail, then tail cannot be in the same relation with r.
[46:43] It will always be symmetric, it won't be able to capture this type of antisymmetry. And then the same thing is with inverse relations,
[46:55] where you would want to be able to enforce relationships with where if head is in relation r2 with tail, then tail is in relation of r1 with the head.
[47:08] And again, because of this argument on the previous slide, DistMult won't be able to model this type of relations because if it does model inverse relations, then it would mean that r1 and r2 have to be the same vector.
[47:25] But semantically, this does not make sense because embedding of advisor shouldn't be the same or should be different than the embedding of the advisee. That's what I wanted to say about modeling inverse
[47:39] relations. And the last thing I want to address is the notion of composition of relations. So here, the question is, can DistMult learn patterns where this r1 composition
[47:54] or transitive relations? The intuition here is that DistMult defines a hyperplane for each head, relation pair, and the union of hyperplanes induced by the multi-hop relationship across multiple
[48:10] relations cannot be expressed as a single hyperplane. So you cannot compose these hyperplanes step by step
[48:22] and maintain the hyperplane. So you won't be able to learn these compositions where you can go or transitivities across relationships.
[48:38] I have a detailed derivation here as well, where, basically, what we are going-- what you are basically able to show is that the composition
[48:56] of two relationship cannot be expressed using a single hyperplane. And the detailed derivation would go in the following way
[49:08] that we would pick some y, such that the scoring function of x, y according to relation 1 is greater than 0. For example, let's call this y2, and then we
[49:23] are going to say that then y2 times some other relation R is going to define the new hyperplane. And then we will be observing what
[49:36] is happening as we now pick another, in our case, another y, such that the relation y and that y is greater than zero, let's call this y3.
[49:51] And then y times the relation 2 will define the new hyperplane. Then, basically, now if you have the two hyperplanes
[50:03] defined by y2 and y3. And now combining them together for all z's that are in this shadow area.
[50:21] The question is, does there exist y between these y2 and y3, such that the score of y and z according to the relation 2 is greater than zero?
[50:39] What you are going to find is that, basically, you cannot find such a case where this would be possible.
[50:57] A way to look at it is that, basically, according to the composition of relations, we would also want the score according now to r3, between x and z, to be greater than zero for every z
[51:12] that is in this shadow area. But this inherently cannot be done or expressed as a single hyperplane defined by x and r3 no matter what r3 is.
[51:28] So basically, this means that, in DistMult, you are not able to express a transitive relations. This is quite interesting because DistMult,
[51:43] as I'm going to show you later, in some knowledge graphs, it works really well. So it becomes a good question, what kind of method to apply to a given domain or to a given knowledge graph?
[51:59] Yes, a question. The key difference between this method we're learning in TransR and TransE seems to be the scoring function. And that's seems then to imply why we can't have this composition, why there's a limitation to composition.
[52:12] Is there a way to pick a scoring method, such that it has many of the beneficial properties of this without the drawback of composition being unavailable? Great. It's a good-- first, I'll repeat your question and also
[52:28] your observation. So observation is that, basically, what we are doing here, this is very similar to our TransE method. We are learning an embedding of every entity and every relation.
[52:41] But what we changed was the scoring function. In the TransE, our scoring function was the distance between h plus r and t. Here, our scoring function is this product
[52:53] and some of these coordinates. And because we changed the scoring function, we get certain properties for free while losing other properties. As I think you are going to see at the end in the final table,
[53:09] it's actually the TransR that checks the most of those check marks, where we were learning this projection matrices between the two vector spaces. That's what I would say about this.
[53:22] Yes. Third question. We were talking today mostly about the transductive setting for most of this learning. But, let's say, in real world application, we saw these are massive, massive, massive, massive networks. So don't we want to basically find a method
[53:35] that we can do on a small part of the network so we can generalize? So let's say, TransR, we'll need the matrix for all of these entries, so that would be a non-computationally feasible matrix.
[53:47] Good question. So the question is these methods are transductive. It means we have to learn an embedding for every entity separately. Won't these be computationally expensive?
[54:00] The answer is yes. I would say from-- the one reason why transductive is OK is because these graphs, we don't think of them as dynamic, we don't think of this as data, we think of this as knowledge
[54:15] in some sense. And the set of entities is fixed, the set of relationships is also fixed, and you are trying to infer, let's say, the edges. You are trying to embed the entities according
[54:28] to the relationships in which they are. Actually, in terms of scalability, this is challenging, but it's not that challenging.
[54:41] Because you can distribute these entities across different machines. And there is a very nice package open sourced by Facebook called Big Graph. If you just Google that on GitHub,
[54:54] you can basically get a system that will allow you to embed essentially arbitrary knowledge graphs. And internally, Facebook, let's say, was using this type of technology
[55:08] to embed all the entities in their knowledge graph and use that for recommendations. So people have put immense resources and energy to be able to scale this up to the Facebook scale,
[55:21] and then they open source. So you can do this and a lot of people, when they want to start playing in industrial settings with graph machine learning use cases, the first thing would be to use this Big Graph package.
[55:34] That's on Facebook. On GitHub. Cool. Does that answer the question? OK, great. Thank you. Super. Now, the last method today, and then we wrap up.
[55:48] This method that I want to talk today, the last one is called ComplEx. It's based on this DisMult, but ComplEx is going to embed entities and relations in the ComplEx vector
[56:02] space. So not in the real, but in the ComplEx. So now, the way you can think of this and what you are getting when you are in the ComplEx space,
[56:15] you get this notion of the complex conjugate. If I have a point with a complex embedding that has the real and the imaginary axis,
[56:27] then there is also exists a conjugate of that point, where, basically, if I had before a plus bi, now I have a minus bi.
[56:40] That's what you get here when you think about ComplEx arithmetics and trying to think about how would I embed things in the ComplEx space.
[56:53] Here, the way we think of this is u is a point in the ComplEx space. And the way the position of it is defined in two ways is defined by the embedding of a and it's
[57:08] defined by the embedding of b and both are k-dimensional. So that's the way to think of this. But of course, what is going to work differently
[57:22] is now the scoring function. And the way the scoring function is going to work is that, now, when I'm doing my scoring function, it's going to be defined this way.
[57:35] So I'm going to multiply h and r, but I'm going to multiply that with the conjugate of t. And then whatever is the result, I'm only going to take the real part of that
[57:47] and that will be my example of the score for a given relation, head, and the tail. That's the idea of how ComplEx is going to work.
[58:03] Now, let's go and look what this will allow us to model. First, let's look at antisymmetric relations. The claim is that ComplEx can model antisymmetric relations.
[58:19] The idea is that the model is expressive enough to be able to learn a high value of the scoring function when you are multiplying h and the conjugate of t,
[58:36] and a low value of the function where you are multiplying t with the conjugate of h. Due to the symmetric modeling of using complex conjugate.
[58:52] This means that we will be able to model ComplEx relationships. How about symmetric relationships, roommate brother, and so on?
[59:05] You are able to do that as well. Here, I have a bit of algebra. So you are asking, what's the score of r, h, and t, and is that the same as the score of r, t, and h?
[59:20] The way you can derive this is to say, oh, this is the real of this product, you can take the product out, you
[59:34] can then take an r, which is a real vector, and just take the real of the h and t, which are complex.
[59:50] If you do it this way, then you can move the conjugate from t to h as well, and then basically expand it back
[1:00:04] to get to the scoring function of t comma h. So the key step is this step where you basically is the equivalence from here to here, and then it's just expanding it back
[1:00:18] to what the scoring function is. So this is for showing symmetric relations. Last, what is interesting about ComplEx is that you can also do inverse relations.
[1:00:33] And the way you can do inverse relations is that r1 is just a conjugate of r-- is a complex conjugate of r2.
[1:00:47] The idea here is in this-- when we talked about cosine distance or cosine similarity where 90 degrees is exactly the angle at which
[1:01:02] things are at the maximum distance. And that's why this is the case here. If you think about-- if you go back to my original picture, the angle between these two vectors, vectors of u
[1:01:18] and the conjugate of u, is also 90 degrees. And the dot product between these two guys will be zero, if you think of it in the Euclidean way.
[1:01:32] So that that's the reason about inverse relations. Then, the last thing I want to talk is about composition as well as one to many relations.
[1:01:45] Here, basically, I can just say that ComplEx shares the same property with DistMult. You cannot model compositional relations and you cannot model one to many relations using it.
[1:01:58] Now, to bring everything together and summarize it, here is a one slide summary of today's lecture of different methods. How do these methods differ? These methods differ on how the embedding is determined.
[1:02:11] Is it determined-- are the embedding h, t, and r in the real space, this was in TransE. In TransR, we had h, t, and r embedded--
[1:02:27] actually, h and t were embedded in d-dimensional, r was embedded in d-dimensional. And then we had the projection matrix that mapped from the entity space to the relation space.
[1:02:40] And then for DistMult and ComplEx. In DistMult, we used the embeddings that were in the reals. For ComplEx, we use the embeddings that were in the complex space, and then
[1:02:53] the scoring functions we were using were different. For TransE, it's a simple, let's say, here, Euclidean distance, the L2 norm between hat plus relation minus tail.
[1:03:05] So basically, the distance between the head plus relation and the tail. In the TransR, we had these projection matrices involved, but it's still, let's say, Euclidean distance. In DistMult, we defined this notion of cosine distance.
[1:03:24] And in ComplEx, we changed further the definition, we adopted the DistMult distance function, but added the-- we extended it in the following way.
[1:03:38] And then what was different is that we looked at these symmetric, antisymmetric, inverse, composite, or also called transitive relations, and one to many relations. And this is how different methods
[1:03:50] compare to what they are able to what relations they are able to model. That's what I wanted to say. And I'm also going to have a few more slides with practical tips
[1:04:05] but, I'm happy now to take questions. I had a question about the antisymmetric case for ComplEx. Is there a ComplEx conjugate interpretation or proving
[1:04:18] that that one works? I just felt like full symmetric [INAUDIBLE],, that was a really nice complex conjugate interpretation. But I didn't get that antisymmetric case.
[1:04:31] Good point. Why don't we then go back and look at it together after the lecture? OK, good. Anything else people would like to ask? If not, let me just a few more things to say.
[1:04:49] In practice, I gave you these methods, and you are like, it's clear what I should be using, it has all the check marks, beautiful. It seems DistMult, you shouldn't really be using, has the most captures the least of these properties and so on.
[1:05:05] But actually, the real world is a bit more complicated. And it actually turns out that different knowledge graphs will have very different, drastically different relation
[1:05:18] patterns, relations with different properties. So generally, there is not one best embedding that works for all different knowledge graphs.
[1:05:33] So many times, it's good to actually go into the knowledge graph, see what are the types of relationships you have, try to quantify them, understand them, and then choose your method.
[1:05:45] What people like to use is usually first run TransE because it's so simple and so easy, it's the easiest to learn, the easiest to make stable. It's the very natural, very interpretable, very easy
[1:06:01] to try. So people would usually start with TransE, and then you can move to more complex models
[1:06:14] like ComplEx, RotatE, DistMult, and so on. TransE is going to work well, especially if your graph doesn't have too many symmetric relations.
[1:06:32] So to summarize today's lecture, we talked about link prediction or knowledge graph completion as one of the important tasks in this field of knowledge graph
[1:06:45] embeddings. We talked about definition of a knowledge graph and how knowledge graphs are being used to serve information, but that knowledge graphs are extremely incomplete.
[1:06:59] And people usually want to complete them, make them more robust. What is also a very useful way to use a knowledge graph is that you can use it as a scaffold for some external
[1:07:12] nodes to connect to it, and then learn a GNN that goes between your data graph and between your background knowledge graph. This is especially very useful in biomedical applications,
[1:07:25] where you have the background biomedical knowledge graph of your biological entities. But maybe, then, you have a patient node that links to different parts of the knowledge graph. And then you can start thinking about learning,
[1:07:39] let's say, GNNs that are going to go from patient down to the knowledge graph, propagate across the knowledge graph, and go back to the patient and do this triangular information passing. And that's a very effective way how you can, let's say,
[1:07:54] reason about patients by exploiting the background knowledge, the background knowledge graph that you have about human biology. That's maybe one way to think about is that knowledge
[1:08:07] graphs are very helpful, either to serve information, and then you want to use these embeddings to complete them. Sometimes people apply this knowledge graph embedding techniques also to their data graphs.
[1:08:20] I mentioned the example of Facebook, and the Big Graph package they developed. But I think when these things work also really well is when you bring your data entities
[1:08:32] and connect them with your knowledge graph entities. This example of patients and underlying biomedical knowledge graphs being an example.
[1:08:46] Today, we talked about-- the lecture today was quite dense, and we talked about four different methods, TransE that's easy and natural. We talked about TransR that's a bit more advanced but based
[1:08:59] on the same intuition. And then DistMult and ComplEx that changed this scoring function. And they all use different embedding spaces, and they have different expressiveness.
[1:09:15] So this is what I wanted to show today. And then next week on Tuesday, I'm actually going to enrich this notion of how do I link prediction in knowledge graphs,
[1:09:29] and we'll talk about these multi-hop link prediction, or basically being able to reason and answer arbitrary queries over incomplete knowledge graph. So we will be given a knowledge graph and a logical query.
[1:09:42] And the question will be, can we find all the entities that satisfy that logical query? That's what we are going to learn about on Tuesday. Let's finish here. But if people have questions, please come here
[1:09:56] and we can talk. Thank you so much.
