# this program creates a network graph of the Lord of the Rings Risk board game
# different colors indicate different regions that they are connected to

# October 17th, 2018


import networkx as nx
import matplotlib.pyplot as plt



####################################################################################################



def add_nodes(graph , node_list , color):

    # add the nodes to the graph
    graph.add_nodes_from(node_list)

    pos = nx.kamada_kawai_layout(graph)

    # format the nodes that are drawn on the graph
    nx.draw_networkx_nodes(graph , pos , nodelist=node_list , node_color=color)



####################################################################################################



def add_edges(graph , edge_list):

    graph.add_edges_from(edge_list)

    pos = nx.kamada_kawai_layout(graph)

    # format the edges that are drawn on the graph
    nx.draw_networkx_edges(graph , pos , edgelist=edge_list)



####################################################################################################



def main():

    G = nx.Graph()
    pos = nx.spring_layout(G)


####################################################################################################

    # nodes (territories) separated by their region on the board



    # Arnor
    arnor_nodes = [ "Angmar" , "Borderlands" , "Buckland" , "Eastern Angmar" , "Fornost" , "Forodwaith" , "North Downs" , "Old Forest" , "Rhudaur" , "South Downs" , "Weather Hills" ]
    nx.draw_networkx_nodes(G, pos,
                           nodelist=arnor_nodes,
                           node_color='black',
                           node_size=500,
                           alpha=0.8)

    # Rhovanion
    rhovanion_nodes = [ "Brown Lands" , "Dead Marshes" , "Emyn Muil" , "Gladden Fields" , "Lorien" , "Moria" , "Rhun Hills" , "The Wold" ]
    nx.draw_networkx_nodes(G, pos,
                           nodelist=rhovanion_nodes,
                           node_color='grey',
                           node_size=500,
                           alpha=0.8)

    # Rohan
    rohan_nodes = [ "Dunland" , "Enedwaith" , "Eregion" , "Fangorn" , "Gap of Rohan" , "Minhiriath" , "West Rohan"]
    nx.draw_networkx_nodes(G, pos,
                           nodelist=rohan_nodes,
                           node_color='brown',
                           node_size=500,
                           alpha=0.8)

    # Mirkwood
    mirkwood_nodes = [ "Anduin Valley" , "Carrock" , "Eastern Mirkwood" , "North Mirkwood" , "South Mirkwood" ]
    nx.draw_networkx_nodes(G, pos,
                           nodelist=mirkwood_nodes,
                           node_color='red',
                           node_size=500,
                           alpha=0.8)

    # Eriador
    eriador_nodes = [ "Evendim Hills" , "Forlindon" , "Harlindon" , "Lune Valley" , "Mithlond" , "The Shire" , "Tower Hills" ]
    nx.draw_networkx_nodes(G, pos,
                           nodelist=eriador_nodes,
                           node_color='darkorange',
                           node_size=500,
                           alpha=0.8)

    # Rhun
    rhun_nodes = [ "Esgaroth" , "North Rhun" , "South Rhun" , "Weathered Heath" ]
    nx.draw_networkx_nodes(G, pos,
                           nodelist=rhun_nodes,
                           node_color='yellow',
                           node_size=500,
                           alpha=0.8)

    # Gondor
    gondor_nodes = [ "Andrast" , "Anfalas" , "Belfalas" , "Druwaith Iaur" , "Ithilien" , "Lamedon" , "Lebennin" , "Minas Tirith" , "South Ithilien" , "Vale of Erech" ]
    nx.draw_networkx_nodes(G, pos,
                           nodelist=gondor_nodes,
                           node_color='seagreen',
                           node_size=500,
                           alpha=0.8)

    # Mordor
    mordor_nodes = [ "Barad-dur" , "Gorgoroth" , "Minas Morgul" , "Mount Doom" , "Nurn" , "Udun Vale" ]
    nx.draw_networkx_nodes(G, pos,
                           nodelist=mordor_nodes,
                           node_color='deeppink',
                           node_size=500,
                           alpha=0.8)

    # Haradwaith
    haradwaith_nodes = [ "Deep Harad" , "Harad" , "Harondor" , "Khand" , "Near Harad" , "Umbar" ]
    nx.draw_networkx_nodes(G, pos,
                           nodelist=haradwaith_nodes,
                           node_color='blue',
                           node_size=500,
                           alpha=0.8)

    ####################################################################################################

    # edges (borders) on the board



    # self-contained edges, i.e. edges that are between two nodes in the same region

    # Arnor
    edges_1 = [
        ("Eastern Angmar" , "Forodwaith") ,
        ("Forodwaith" , "Angmar") , ("Forodwaith" , "Borderlands") ,
        ("Angmar" , "Borderlands") ,
        ("Borderlands" , "North Downs") , ("Borderlands" , "Fornost") , ("Borderlands" , "Weather Hills") ,
        ("North Downs" , "Fornost") ,
        ("Fornost" , "Buckland") , ("Fornost" , "Old Forest") , ("Fornost" , "Weather Hills") ,
        ("Buckland" , "Old Forest") , ("Buckland" , "South Downs") ,
        ("Old Forest" , "South Downs") , ("Old Forest" , "Weather Hills") ,
        ("Weather Hills" , "South Downs") , ("Weather Hills" , "Rhudaur")
                ]


    # Rhovanion
    edges_2 = [
        ("Moria" , "Gladden Fields") ,
        ("Gladden Fields" , "Lorien") ,
        ("Lorien" , "The Wold") ,
        ("The Wold" , "Emyn Muil") ,
        ("Emyn Muil" , "Dead Marshes") , ("Emyn Muil" , "Brown Lands") ,
        ("Brown Lands" , "Dead Marshes") , ("Brown Lands" , "Rhun Hills")
               ]



    # Rohan
    edges_3 = [
        ("Eregion" , "Dunland") ,
        ("Dunland" , "Minhiriath") , ("Dunland" , "Enedwaith") ,
        ("Enedwaith" , "Minhiriath") , ("Enedwaith" , "Gap of Rohan") ,
        ("Gap of Rohan" , "West Rohan") , ("Gap of Rohan" , "Fangorn")
               ]



    # Mirkwood
    edges_4 = [
        ("Carrock" , "North Mirkwood") , ("Carrock" , "Anduin Valley") ,
        ("North Mirkwood" , "Eastern Mirkwood") ,
        ("Eastern Mirkwood" , "Anduin Valley") , ("Eastern Mirkwood" , "South Mirkwood") ,
        ("South Mirkwood" , "Anduin Valley")
               ]



    # Eriador
    edges_5 = [
        ("Forlindon" , "Mithlond") ,
        ("Mithlond" , "Lune Valley") , ("Mithlond" , "Tower Hills") , ("Mithlond" , "Harlindon") ,
        ("Lune Valley" , "Evendim Hills") , ("Lune Valley" , "Tower Hills") ,
        ("Evendim Hills" , "Tower Hills") ,
        ("Tower Hills" , "The Shire")
                ]



    # Rhun
    edges_6 = [
        ("North Rhun" , "Weathered Heath") , ("North Rhun" , "South Rhun") ,
        ("Weathered Heath" , "Esgaroth")
               ]



    # Gondor
    edges_7 = [
        ("Druwaith Iaur" , "Anfalas") ,
        ("Anfalas" , "Andrast") , ("Anfalas" , "Vale of Erech") ,
        ("Vale of Erech" , "Lamedon") ,
        ("Lamedon" , "Belfalas") , ("Lamedon" , "Lebennin") ,
        ("Lebennin" , "Belfalas") , ("Lebennin" , "Minas Tirith") ,
        ("Minas Tirith" , "Ithilien") ,
        ("Ithilien" , "South Ithilien")
               ]



    # Mordor
    edges_8 = [
        ("Udun Vale" , "Mount Doom") ,
        ("Mount Doom" ,"Barad-dur") , ("Mount Doom" , "Gorgoroth") ,
        ("Gorgoroth" , "Barad-dur") , ("Gorgoroth" , "Minas Morgul") , ("Gorgoroth" , "Nurn")
               ]



    # Haradwaith
    edges_9 = [
        ("Harondor" , "Harad") ,
        ("Harad" , "Deep Harad") , ("Harad" , "Near Harad") ,
        ("Deep Harad" , "Umbar") ,
        ("Near Harad" , "Khand")
               ]





    # edges between different nodes (territories) in different regions

    edges_misc = [
        ("Forodwaith" , "Mithlond") , ("Forodwaith" , "North Rhun") , ("Forodwaith" , "Weathered Heath") ,
        ("Eastern Angmar" , "Carrock") ,
        ("Borderlands" , "Lune Valley") , ("Borderlands" , "Evendim Hills") ,
        ("Buckland" , "The Shire") ,
        ("South Downs" , "Minhiriath") ,
        ("Rhudaur" , "Eregion") , ("Rhudaur" , "Carrock") ,
        ("Moria" , "Eregion") ,
        ("Gladden Fields" , "Anduin Valley") ,
        ("Lorien" , "Fangorn") ,
        ("The Wold" , "Fangorn") , ("The Wold" , "Gap of Rohan") ,
        ("Emyn Muil" , "Anduin Valley") , ("Emyn Muil" , "South Mirkwood") ,
        ("Brown Lands" , "South Mirkwood") , ("Brown Lands" , "Eastern Mirkwood") , ("Brown Lands" , "South Rhun") ,
        ("Dead Marshes" , "Ithilien") , ("Dead Marshes" , "Udun Vale") ,
        ("Minhiriath" , "Mithlond") , ("Minhiriath" , "Belfalas") , ("Minhiriath" , "Umbar") ,
        ("West Rohan" , "Druwaith Iaur") ,
        ("Gap of Rohan" , "Minas Tirith") ,
        ("North Mirkwood" , "Esgaroth") ,
        ("Ithilien" , "Minas Morgul") ,
        ("South Ithilien" , "Harondor") ,
        ("Belfalas" , "Umbar")
                  ]



    # all of the edges in the game
    all_edges = edges_1 + edges_2 + edges_3 + edges_4 + edges_5 + edges_6 + edges_7 + edges_8 + edges_9 + edges_misc

    nx.draw_networkx_edges(G, pos,
                           edgelist=all_edges,
                           width=8, alpha=0.5)


####################################################################################################

    # show the graph of the game

    nx.draw_kamada_kawai(G)
    plt.show()

####################################################################################################

main()