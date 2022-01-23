//
//  ListRowView.swift
//  slackr
//
//  Created by Harshul Jain on 1/22/22.
//

import SwiftUI

struct ListRowView: View {
    
    let item: ItemModel
    
    
    var body: some View {
        HStack{
            Image(systemName: "checkmark.circle")
                .foregroundColor(.green)
            Text(item.title)
                .fontWeight(.ultraLight)
                .foregroundColor(Color.black).background(Color.clear)
            Spacer()
        }
        .font(.title3)
        .padding(.vertical, 8)
    }
}

struct ListRowView_Previews: PreviewProvider {
    
    static var item1 = ItemModel(title: "First")
    static var item2 = ItemModel(title: "Second Item")
    
    static var previews: some View {
        Group{
            ListRowView(item: item1)
            ListRowView(item: item2)
        }
    }
}
