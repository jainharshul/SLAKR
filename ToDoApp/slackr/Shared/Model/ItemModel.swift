//
//  ItemModel.swift
//  slackr
//
//  Created by Harshul Jain on 1/22/22.
//

import Foundation

struct ItemModel: Identifiable, Codable{
    let id: String = UUID().uuidString
    let title: String

}
